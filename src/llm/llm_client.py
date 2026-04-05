from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path

# 🔥 Force correct path
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")

#print("Loaded API Key:", api_key)
print("ENV PATH:", env_path)

if not api_key or api_key == "your_api_key_here":
    raise ValueError("❌ GROQ API KEY NOT LOADED PROPERLY")

client = Groq(api_key=api_key)

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",   
        messages=[
            {"role": "system", "content": "Give professional, concise answers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content