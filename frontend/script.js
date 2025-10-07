const form = document.getElementById("resumeForm");
const resumeOutput = document.getElementById("resumeOutput");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        skills: document.getElementById("skills").value.split(","), // convert to array
        education: document.getElementById("education").value,
        projects: document.getElementById("projects").value
    };

    try {
        // Generate resume
        const response = await fetch("http://127.0.0.1:5000/generate_resume", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if(result.file_ready){
            resumeOutput.innerHTML = `
                Resume generated successfully! <br>
                <a href="http://127.0.0.1:5000/download_resume" target="_blank">Click here to download</a>
            `;
        } else {
            resumeOutput.textContent = "Error generating resume.";
        }
    } catch (err) {
        console.error(err);
        resumeOutput.textContent = "Error generating resume. Check backend.";
    }
});
