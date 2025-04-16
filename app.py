from flask import Flask, render_template, url_for, request, redirect, url_for
import os
import fitz
import joblib
import re
import string
from webscrap import vacancies
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return "No file part", 400

    file = request.files['pdf_file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Extract text from the PDF
        text = extract_pdf_text(filepath)
        job = translate_job_category(text)
        link = extract_links(text)
        return render_template('result.html', filename=file.filename, text=job, link=link)

    return "Invalid file type. Only PDFs are allowed.", 400

global text


def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

def classify_resume(cv_text):
    cv_text = clean_text(cv_text)
    model = joblib.load("save_model.pkl")
    prediction = model.predict([cv_text])
    predicted_job = prediction[0]
    return predicted_job

def extract_links(name):
    links = vacancies(name)
    return links

def translate_job_category(category):
    if category == "HR":
        return "Resurse Umane"
    elif category == "DESIGNER":
        return "Designer"
    elif category == "INFORMATION-TECHNOLOGY":
        return "Tehnologia Informației"
    elif category == "TEACHER":
        return "Profesor"
    elif category == "ADVOCATE":
        return "Avocat"
    elif category == "BUSINESS-DEVELOPMENT":
        return "Dezvoltare Afaceri"
    elif category == "HEALTHCARE":
        return "Îngrijire Sănătate"
    elif category == "FITNESS":
        return "Fitness"
    elif category == "AGRICULTURE":
        return "Agricultură"
    elif category == "BPO":
        return "Externalizare Procese de Afaceri"
    elif category == "SALES":
        return "Vânzări"
    elif category == "CONSULTANT":
        return "Consultant"
    elif category == "DIGITAL-MEDIA":
        return "Media Digitală"
    elif category == "AUTOMOBILE":
        return "Automobile"
    elif category == "CHEF":
        return "Bucătar"
    elif category == "FINANCE":
        return "Finanțe"
    elif category == "APPAREL":
        return "Îmbrăcăminte"
    elif category == "ENGINEERING":
        return "Inginerie"
    elif category == "ACCOUNTANT":
        return "Contabil"
    elif category == "CONSTRUCTION":
        return "Construcții"
    elif category == "PUBLIC-RELATIONS":
        return "Relații Publice"
    elif category == "BANKING":
        return "Servicii Bancare"
    elif category == "ARTS":
        return "Arte"
    elif category == "AVIATION":
        return "Aviație"

def extract_pdf_text(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
        job = classify_resume(text)
    return job if job else "No readable text found."
    

if __name__ == "__main__":
    app.run(debug=True)