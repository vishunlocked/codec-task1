# 📄 Automated Resume Parser

> A Flask-based web application to upload, extract, and manage resumes using NLP and PostgreSQL — built as part of the Codec Technologies Internship.

---

## 📌 Table of Contents

- [📄 Project Description](#-project-description)
- [🚀 Features](#-features)
- [🧱 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🗄️ PostgreSQL Database Setup](#️-postgresql-database-setup)
- [📦 Python Dependencies](#-python-dependencies)
- [🧪 Running the App](#-running-the-app)
- [📸 Screenshots](#-screenshots)
- [✅ Future Improvements](#-future-improvements)
- [🛡️ Security Notice](#️-security-notice)
- [📃 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📄 Project Description

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

## 🚀 Features

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

## 🧱 Tech Stack

### 💻 Backend
- Python 3.x
- Flask
- spaCy (NLP processing)
- psycopg2 (PostgreSQL connector)
- pdfplumber (PDF text extraction)
- PyMuPDF (`fitz` library for fast PDF reading in `extract_resume.py`)
- re (Regex for pattern extraction)

### 🗄️ Database
- PostgreSQL

### 🌐 Frontend (Templates)
- HTML5
- Jinja2 (Flask template engine)

---

## 📁 Project Structure
codec-task1/
│
├── templates/ # HTML templates
│ ├── upload.html # Upload page
│ ├── result.html # Parsed results
│ ├── list.html # View all resumes
│ └── edit.html # Edit a resume entry
│
├── app.py # Main Flask app with routes and logic
├── extract_resume.py # REST-style extractor using fitz (PyMuPDF)
├── vishnuresume.pdf # Sample PDF used for testing
├── pycache/ # Python cache files
└── README.md # Project documentation (this file)

2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv

# For Linux/Mac:
source venv/bin/activate

# For Windows:
venv\Scripts\activate

3️⃣ Install Required Packages
If you have a requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Otherwise, manually install:

bash
Copy
Edit
pip install Flask psycopg2-binary spacy pdfplumber PyMuPDF
python -m spacy download en_core_web_sm
🗄️ PostgreSQL Database Setup
✅ Step 1: Create Database
Use psql or PgAdmin:

sql
Copy
Edit
CREATE DATABASE resume_db;
✅ Step 2: Create resumes Table
sql
Copy
Edit
CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    skills TEXT,
    education TEXT
);
✅ Step 3: Update Credentials in Code
In both app.py and extract_resume.py, update this block with your DB credentials:

python
Copy
Edit
psycopg2.connect(
    dbname="resume_db",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)
📦 Python Dependencies
Package	Purpose
Flask	Web framework for routing and templating
spaCy	NLP for extracting names and entities
pdfplumber	PDF text extraction from uploaded files
PyMuPDF (fitz)	Alternative fast PDF parser (API version)
psycopg2-binary	PostgreSQL integration with Python
re	Regex for email/phone matching

🧪 Running the App
▶️ Option 1: Run Flask Web App
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

▶️ Option 2: Run API Resume Extractor
bash
Copy
Edit
python extract_resume.py
Use Postman or cURL to test:

h
Copy
Edit
POST /upload
Content-Type: multipart/form-data
Body: resume (PDF file)
Response (JSON):

json
Copy
Edit
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+919999999999"
}
📸 Screenshots
(Add screenshots here manually in GitHub later if needed)

Upload Resume: Choose and upload your resume

Result View: Extracted Name, Email, Phone, Skills, Education

Resume List: View all parsed resumes from DB with actions

Edit Resume: Manually update extracted info

✅ Future Improvements
 Add support for .docx using python-docx

 Support image-based resumes via OCR (e.g., Tesseract)

 Improve NLP parsing using Transformer models (e.g., BERT)

 Add file size/type validation

 Add user login and admin panel (Flask-Login)

 Export data to CSV/JSON

 Add Docker for containerized deployment



