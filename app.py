import streamlit as st
import requests

# Function to talk to Ollama
def ask_ai(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )
    return response.json()["response"]


st.title("🤖 AI Resume Assistant")

# Inputs
job_role = st.text_input("Target Job Role")
name = st.text_input("Full Name")
education = st.text_area("Education")
experience = st.text_area("Work Experience")
skills = st.text_area("Current Skills")
projects = st.text_area("Projects")
achievements = st.text_area("Achievements")

# SINGLE BUTTON ONLY
if st.button("Generate Resume"):

    prompt = f"""
Create a professional ATS-friendly resume.

Candidate Details

Name: {name}
Target Job Role: {job_role}

Education:
{education}

Work Experience:
{experience}

Skills:
{skills}

Projects:
{projects}

Achievements:
{achievements}

Generate the resume with the following sections:

1. Professional Summary
2. Work Experience
3. Skills
4. Soft Skills
5. Technical Skills
6. Achievements
7. Projects

Rules:
- Do NOT invent information
- Improve wording
- Use bullet points
- Make it ATS-friendly
"""

    result = ask_ai(prompt)

    st.subheader("Generated Resume")
    st.write(result)

    st.download_button(
        label="Download Resume",
        data=result,
        file_name="resume.txt",
        mime="text/plain"
    )