from flask import Flask, request, send_file, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pdfkit
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

# wkhtmltopdf setup
wkhtmltopdf_path = os.getenv("WKHTMLTOPDF_PATH")  # from .env
pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

last_resume_path = None

# Serve frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

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

        html_content = f"""<html>...same as before...</html>"""  # Use your HTML template here

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
