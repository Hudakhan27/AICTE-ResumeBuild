from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import pdfkit
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# wkhtmltopdf setup
wkhtmltopdf_path = os.getenv("WKHTMLTOPDF_PATH")  # from .env
pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

# Store last generated PDF path
last_resume_path = None

# Home route (optional)
@app.route('/')
def home():
    return "Flask backend is running!"

# Generate resume
@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    global last_resume_path
    try:
        data = request.get_json()
        name = data.get("name", "Unknown")
        email = data.get("email", "")
        skills = data.get("skills", [])
        education = data.get("education", "")
        projects = data.get("projects", "")

        # ATS-friendly HTML template
        html_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{name} - Resume</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    font-size: 12pt;
                    margin: 40px;
                    line-height: 1.4;
                    color: #000;
                }}
                h1 {{
                    font-size: 20pt;
                    margin-bottom: 0;
                }}
                h2 {{
                    font-size: 14pt;
                    margin-bottom: 5px;
                    margin-top: 20px;
                    border-bottom: 1px solid #000;
                }}
                p, li {{
                    margin: 5px 0;
                }}
                ul {{
                    padding-left: 20px;
                }}
                .section {{
                    margin-bottom: 15px;
                }}
            </style>
        </head>
        <body>
            <h1>{name}</h1>
            <p><strong>Email:</strong> {email}</p>

            <div class="section">
                <h2>Education</h2>
                <p>{education}</p>
            </div>

            <div class="section">
                <h2>Skills</h2>
                <ul>
                    {''.join(f"<li>{skill}</li>" for skill in skills)}
                </ul>
            </div>

            <div class="section">
                <h2>Projects</h2>
                <ul>
                    {''.join(f"<li>{project}</li>" for project in projects.split(','))}
                </ul>
            </div>
        </body>
        </html>
        """

        # Save PDF
        output_path = os.path.join(os.getcwd(), "resume.pdf")
        pdfkit.from_string(html_content, output_path, configuration=pdfkit_config)
        last_resume_path = output_path

        return jsonify({"file_ready": True})

    except Exception as e:
        print("Error generating resume:", e)
        return jsonify({"error": "Error generating resume"}), 500

# Download resume
@app.route('/download_resume', methods=['GET'])
def download_resume():
    if last_resume_path and os.path.exists(last_resume_path):
        return send_file(last_resume_path, as_attachment=True, download_name="resume.pdf")
    return jsonify({"error": "No resume found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
