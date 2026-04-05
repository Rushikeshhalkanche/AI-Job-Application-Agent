from src.llm.llm_client import ask_llm

def tailor_resume(profile, job_desc):
    prompt = f"""
Tailor this resume for the job.

Profile:
{profile}

Job Description:
{job_desc}
"""
    return ask_llm(prompt)