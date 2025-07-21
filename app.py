from flask import Flask, request, render_template, redirect, url_for
import pdfplumber
import spacy
import re
import psycopg2

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

BAD_NAME_KEYWORDS = {
    "python", "java", "c++", "developer", "engineer", "project",
    "email", "phone", "address", "resume", "experience", "skills"
}
SKILLS_KEYWORDS = ['Python', 'Java', 'SQL', 'Machine Learning', 'Communication', 'Leadership', 'Excel', 'AWS', 'Docker', 'JavaScript', 'HTML', 'CSS']
EDUCATION_KEYWORDS = ['Bachelor', 'Master', 'B.Tech', 'M.Tech', 'MBA', 'PhD', 'High School', 'Diploma', 'Certification']

# --- Helper Functions ---

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_info(text):
    lines = text.split("\n")
    top_text = "\n".join(lines[:10])
    top_doc = nlp(top_text)

    # Name Extraction
    name = None
    for ent in top_doc.ents:
        if ent.label_ == "PERSON" and ent.text.strip().lower() not in BAD_NAME_KEYWORDS:
            name = ent.text.strip()
            break
    if not name:
        for line in lines[:5]:
            line_lower = line.lower()
            if any(bad in line_lower for bad in BAD_NAME_KEYWORDS):
                continue
            if len(line.strip().split()) >= 2:
                name = line.strip()
                break

    # Email
    email_match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    email = email_match.group(0).strip() if email_match else None

    # Phone
    phone_match = re.search(r'(?:(?:\+91[\-\s]?|0)?[6-9]\d{9})', text)
    phone = phone_match.group(0).strip() if phone_match else None

    # Skills
    skills_found = [skill for skill in SKILLS_KEYWORDS if skill.lower() in text.lower()]
    skills = ', '.join(skills_found) if skills_found else "Not specified"

    # Education
    education_found = [edu for edu in EDUCATION_KEYWORDS if edu.lower() in text.lower()]
    education = ', '.join(education_found) if education_found else "Not specified"

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education
    }

def insert_into_db(data):
    try:
        conn = psycopg2.connect(
            dbname="resume_db",
            user="postgres",
            password="Vishnu@123",  # Change if needed
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO resumes (name, email, phone, skills, education)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("skills"),
            data.get("education")
        ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Database Error:", e)

# --- Flask Routes ---

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files.get('resume')
    if not file:
        return "No file uploaded", 400

    text = extract_text_from_pdf(file)
    info = extract_info(text)
    insert_into_db(info)
    return render_template("result.html", info=info)

@app.route('/resumes')
def list_resumes():
    try:
        conn = psycopg2.connect(
            dbname="resume_db",
            user="postgres",
            password="Vishnu@123",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, phone, skills, education FROM resumes ORDER BY id DESC")
        resumes = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Fetch Error:", e)
        resumes = []
    return render_template("list.html", resumes=resumes)

@app.route('/delete/<int:resume_id>')
def delete_resume(resume_id):
    try:
        conn = psycopg2.connect(
            dbname="resume_db",
            user="postgres",
            password="Vishnu@123",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM resumes WHERE id = %s", (resume_id,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Delete Error:", e)
    return redirect(url_for('list_resumes'))

@app.route('/edit/<int:resume_id>', methods=['GET', 'POST'])
def edit_resume(resume_id):
    conn = psycopg2.connect(
        dbname="resume_db",
        user="postgres",
        password="Vishnu@123",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        skills = request.form.get('skills')
        education = request.form.get('education')
        cur.execute("""
            UPDATE resumes
            SET name=%s, email=%s, phone=%s, skills=%s, education=%s
            WHERE id=%s
        """, (name, email, phone, skills, education, resume_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('list_resumes'))
    else:
        cur.execute("SELECT name, email, phone, skills, education FROM resumes WHERE id=%s", (resume_id,))
        resume = cur.fetchone()
        cur.close()
        conn.close()
        if not resume:
            return "Resume not found", 404
        return render_template("edit.html", resume_id=resume_id, resume=resume)

if __name__ == '__main__':
    app.run(debug=True)
