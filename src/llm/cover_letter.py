from src.llm.llm_client import ask_llm

def generate_cover_letter(profile, job_desc):
    prompt = f"""
Write a professional cover letter.

Profile:
{profile}

Job Description:
{job_desc}
"""
    return ask_llm(prompt)