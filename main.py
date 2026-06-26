from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()

    with open("job_description.txt", "r", encoding="utf-8") as f:
        job = f.read()

    prompt = f"""
You are a professional recruiter.

TASK:
Improve resume based on job description.

RESUME:
{resume}

JOB DESCRIPTION:
{job}

OUTPUT:
1. ATS Score
2. Missing Skills
3. Improved Resume
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    output = response.output_text

    print(output)

    with open("improved_resume.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print("Success: Resume improved!")

except FileNotFoundError as e:
    print("Error: Missing file -", e)

except Exception as e:
    print("Something went wrong:", e)