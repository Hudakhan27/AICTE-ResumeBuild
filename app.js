import React, { useState } from "react";
import axios from "axios";
import html2pdf from "html2pdf.js";

function App() {
  const [form, setForm] = useState({ name: "", email: "", skills: "", education: "", projects: "" });
  const [resume, setResume] = useState("");
  const [coverLetter, setCoverLetter] = useState("");

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const generateResume = async () => {
    const res = await axios.post("http://localhost:5000/generate-resume", form);
    setResume(res.data.resume);
  };

  const generateCoverLetter = async () => {
    const res = await axios.post("http://localhost:5000/generate-cover-letter", { ...form, job_description: "Software Developer Internship" });
    setCoverLetter(res.data.cover_letter);
  };

  const downloadClientPDF = () => {
    const element = document.getElementById("resume-preview");
    if (!element) { alert("No resume rendered"); return; }
    html2pdf().from(element).save(`${form.name || "resume"}_resume.pdf`);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-4">AI Resume & Portfolio Builder</h1>
      <div className="bg-white shadow p-4 rounded-lg space-y-3">
        <input className="border p-2 w-full" name="name" placeholder="Name" onChange={handleChange} />
        <input className="border p-2 w-full" name="email" placeholder="Email" onChange={handleChange} />
        <textarea className="border p-2 w-full" name="skills" placeholder="Skills" onChange={handleChange} />
        <textarea className="border p-2 w-full" name="education" placeholder="Education" onChange={handleChange} />
        <textarea className="border p-2 w-full" name="projects" placeholder="Projects" onChange={handleChange} />
        <button onClick={generateResume} className="bg-blue-500 text-white px-4 py-2 rounded">Generate Resume</button>
        <button onClick={generateCoverLetter} className="bg-green-500 text-white px-4 py-2 rounded ml-2">Generate Cover Letter</button>
      </div>

      {resume && (
        <div id="resume-preview" className="bg-white shadow mt-6 p-4 rounded-lg">
          <h2 className="text-xl font-bold mb-2">Generated Resume</h2>
          <pre className="whitespace-pre-wrap">{resume}</pre>
        </div>
      )}
      {resume && (
        <button onClick={downloadClientPDF} className="bg-gray-700 text-white px-4 py-2 rounded mt-2">Download PDF</button>
      )}

      {coverLetter && (
        <div className="bg-white shadow mt-6 p-4 rounded-lg">
          <h2 className="text-xl font-bold mb-2">Generated Cover Letter</h2>
          <pre className="whitespace-pre-wrap">{coverLetter}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
