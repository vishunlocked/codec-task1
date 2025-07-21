import re
import spacy
from flask import Flask, request, jsonify
import fitz  # PyMuPDF for PDF text extraction

app = Flask(__name__)

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# List of keywords that are NOT names (common programming terms, etc.)
BAD_NAME_KEYWORDS = {
    "java", "python", "developer", "engineer", "software", "application", "project",
    "skills", "education", "experience", "email", "phone", "address"
}

def extract_info(text):
    lines = text.split("\n")
    top_text = "\n".join(lines[:10])
    top_doc = nlp(top_text)

    # Try spaCy to get name
    name = None
    for ent in top_doc.ents:
        if ent.label_ == "PERSON" and ent.text.strip().lower() not in BAD_NAME_KEYWORDS:
            name = ent.text.strip()
            break

    # Fallback: Top line with 2+ words and not a keyword
    if not name:
        for line in lines[:5]:
            line_lower = line.lower()
            if any(bad in line_lower for bad in BAD_NAME_KEYWORDS):
                continue
            if len(line.strip().split()) >= 2:
                name = line.strip()
                break

    # Clean name: remove all caps with spacing (e.g., "K A N D I")
    if name and name.replace(" ", "").isalpha() and name == name.upper():
        name = name.replace(" ", "").title()

    # Extract email
    email_match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    email = email_match.group(0).strip() if email_match else None

    # Extract phone number (Indian style + fallback)
    phone_match = re.search(
        r'(?:(?:\+91[\-\s]?|0)?[6-9]\d{9})',
        text
    )
    phone = phone_match.group(0).strip() if phone_match else None

    return {
        "name": name,
        "email": email,
        "phone": phone
    }


def extract_text_from_pdf(file_stream):
    doc = fitz.open(stream=file_stream.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        text = extract_text_from_pdf(file)
        data = extract_info(text)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
