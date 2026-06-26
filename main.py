import requests

def ask_ai(prompt):
    try:
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

    except Exception as e:
        return f"Error: {e}"


# TEST RUN ONLY
if __name__ == "__main__":
    result = ask_ai("Write a resume summary for a Python developer")
    print(result)