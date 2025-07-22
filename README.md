# Automated Resume Parser

## Project Overview
This project is a web-based system that automatically extracts and categorizes key information from resumes (PDF format). It uses Python libraries such as spaCy for NLP and PDFPlumber or PyMuPDF for PDF text extraction. Extracted data like candidate name, email, phone, skills, and education are stored in a PostgreSQL database for easy searching and editing.

---

## Features
- Upload resumes in PDF format through a web interface
- Automatically extract candidate details (name, email, phone, skills, education)
- Store parsed information in a PostgreSQL database
- List all uploaded resumes with editable fields
- Update or delete stored resume data
- Clean, intuitive HTML templates powered by Flask

---

## Technologies Used
- Python 3.x
- Flask (Web framework)
- spaCy (Natural Language Processing)
- PDFPlumber / PyMuPDF (PDF text extraction)
- PostgreSQL (Database)
- HTML / Jinja2 (Templates)
- psycopg2 (PostgreSQL adapter for Python)

---

## Setup Instructions

### Prerequisites
- Python 3.7+
- PostgreSQL installed and running
- `en_core_web_sm` spaCy model

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/automated-resume-parser.git
   cd automated-resume-parser
2. Create and activate virtual environment
   python -m venv resume_env
source resume_env/bin/activate   # Linux/Mac
resume_env\Scripts\activate      # Windows

3.Install dependencies

pip install -r requirements.txt

flask
spacy
pdfplumber
pymupdf
psycopg2-binary

4. Download spaCy English model

   python -m spacy download en_core_web_sm

5.Setup PostgreSQL database

CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    skills TEXT,
    education TEXT
);

6. Configure database credentials
   python app.py

Project Structure

INTERNPROJECT/
│
├── app.py                 # Flask web app & routes
├── extract_resume.py      # Separate extraction API example
├── templates/
│   ├── upload.html        # Upload form
│   ├── result.html        # Extraction result display
│   ├── list.html          # List stored resumes
│   └── edit.html          # Edit resume data form
├── resume_env/            # Python virtual environment
├── vishnuresume.pdf       # Sample resume file
└── README.md              # This documentation

