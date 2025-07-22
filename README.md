# 📄 Automated Resume Parser

> A Flask-based web application to upload, extract, and manage resumes using NLP and PostgreSQL — built as part of the Codec Technologies Internship.

---

##  Table of Contents

- [ Project Description](#-project-description)
- [ Features](#-features)
- [ Tech Stack](#-tech-stack)
- [ Project Structure](#-project-structure)
- [ Installation & Setup](#️-installation--setup)
- [ PostgreSQL Database Setup](#️-postgresql-database-setup)
- [ Python Dependencies](#-python-dependencies)
- [ Running the App](#-running-the-app)
- [ Screenshots](#-screenshots)
- [ Future Improvements](#-future-improvements)
- [ Security Notice](#️-security-notice)
- [ Acknowledgements](#-acknowledgements)

---

##  Project Description

This is a **Resume Parser** web application developed using **Python, Flask, spaCy, pdfplumber**, and **PostgreSQL**. It allows users to:

- Upload resumes in PDF format
- Automatically extract key information such as:
  - Full Name
  - Email ID
  - Phone Number
  - Skills
  - Education
- Store this information in a PostgreSQL database
- View, edit, or delete entries via a simple web UI

---

##  Features

✅ Upload and parse resumes in `.pdf` format  
✅ Extract personal information using **spaCy NLP**  
✅ Use **regex** for phone number and email parsing  
✅ Filter and categorize using keyword dictionaries  
✅ Store parsed data in a **PostgreSQL** database  
✅ View and manage all stored resumes  
✅ Edit and delete entries from the dashboard  
✅ Clean and user-friendly UI using HTML + Jinja2  
✅ API-style resume extractor using PyMuPDF (in `extract_resume.py`)

---

##  Tech Stack

###  Backend
- Python 3.x
- Flask
- spaCy (NLP processing)
- psycopg2 (PostgreSQL connector)
- pdfplumber (PDF text extraction)
- PyMuPDF (`fitz` library for fast PDF reading in `extract_resume.py`)
- re (Regex for pattern extraction)

###  Database
- PostgreSQL

###  Frontend (Templates)
- HTML5
- Jinja2 (Flask template engine)

---

##  Project Structure

```text
codec-task1/
│
├── templates/               # HTML templates
│   ├── upload.html          # Upload page
│   ├── result.html          # Parsed results
│   ├── list.html            # View all resumes
│   └── edit.html            # Edit a resume entry
│
├── app.py                   # Main Flask app with routes and logic
├── extract_resume.py        # REST-style extractor using fitz (PyMuPDF)
├── vishnuresume.pdf         # Sample PDF used for testing
├── pycache/                 # Python cache files
└── README.md                # Project documentation (this file)

# Installation & Setup

## 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv

For Windows
venv\Scripts\activate

3️⃣ Install Required Packages

pip install -r requirements.txt
pip install Flask psycopg2-binary spacy pdfplumber PyMuPDF
python -m spacy download en_core_web_sm

PostgreSQL Database Setup

✅ Step 1: Create Database
Use psql or PgAdmin:

CREATE DATABASE resume_db;

✅ Step 2: Create resumes Table

CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    skills TEXT,
    education TEXT
);

✅ Step 3: Update Credentials in Code

psycopg2.connect(
    dbname="resume_db",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)

📦 Python Dependencies
| Package         | Purpose                                  |
| --------------- | ---------------------------------------- |
| Flask           | Web framework for routing and templating |
| spaCy           | NLP for extracting names and entities    |
| pdfplumber      | PDF text extraction from uploaded files  |
| PyMuPDF (fitz)  | Alternative fast PDF parser              |
| psycopg2-binary | PostgreSQL integration with Python       |
| re              | Regex for email/phone matching           |


🧪 Running the App

▶️ Option 1: Run Flask Web App

python app.py

▶️ Option 2: Run API Resume Extractor

python extract_resume.py

POST /upload
Content-Type: multipart/form-data
Body: resume (PDF file)

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+919999999999"
}

📸 Screenshots

Upload Resume – Choose and upload your resume

Result View – Extracted Name, Email, Phone, Skills, Education

Resume List – View all parsed resumes from DB with actions

Edit Resume – Manually update extracted info


✅ Future Improvements

Add support for .docx using python-docx

Support image-based resumes via OCR (e.g., Tesseract)

Improve NLP parsing using transformer models like BERT

Add file size/type validation

Add user login and admin panel using Flask-Login

Export parsed data to CSV/JSON

Add Docker support for containerized deployment








