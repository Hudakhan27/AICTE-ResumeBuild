

🧠 AI Resume Builder

The AI Resume Builder is a smart web application that helps users instantly generate professional, ATS-friendly resumes using AI. It combines a responsive frontend and a Flask-based backend to deliver quick, elegant, and downloadable resume PDFs.

🚀 Features

Generate resumes automatically from user input

Download resumes as PDF

Clean and modern user interface

Secure API key management using .env

Flask backend with AI integration

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

AI: OpenAI API

PDF Generation: pdfkit + wkhtmltopdf

Deployment: Render / Streamlit

⚙️ How It Works

User enters details (name, email, education, skills, projects).

Flask backend processes and converts data into a formatted HTML resume.

The HTML is converted into a downloadable PDF file.

User downloads or previews the generated resume.

🧩 Setup

Clone the repository

git clone https://github.com/your-username/ai-resume-builder.git


Install dependencies

pip install -r requirements.txt


Add your .env file

OPENAI_API_KEY=your_openai_api_key
WKHTMLTOPDF_PATH=/usr/bin/wkhtmltopdf


Run the project

python app.py

📦 Deployment

Easily deploy using:

Render (for Flask backend)

Netlify / GitHub Pages (for frontend)
