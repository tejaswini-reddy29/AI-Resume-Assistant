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

job_role = st.text_input("Target Job Role")

name = st.text_input("Full Name")

education = st.text_area("Education")

experience = st.text_area("Work Experience")

skills = st.text_area("Current Skills")

projects = st.text_area("Projects")

achievements = st.text_area("Achievements")

if st.button("Generate Resume Summary"):

 prompt = f"""
Create a professional ATS-friendly resume.

Candidate Details

Name:
{name}

Target Job Role:
{job_role}

Education:
{education}

Work Experience:
{experience}

Current Skills:
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

Write professionally using bullet points.
Do not invent information that wasn't provided.
Improve the wording of the provided information.
"""
if st.button("Generate Resume"):
    result = ask_ai(prompt)

    st.subheader("Generated Resume")

    st.write(result)

st.download_button(
    label="Download Summary",
    data=result,
    file_name="resume_summary.txt",
    mime="text/plain"
)