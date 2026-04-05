from src.llm.resume import tailor_resume
from src.llm.cover_letter import generate_cover_letter
from src.browser.apply import apply_job
from src.ats.detector import detect_ats

def run_agent(job, profile):
    print("Processing:", job)

    ats = detect_ats(job)
    print("ATS:", ats)

    job_desc = "Software Engineer role requiring Python and AI"

    resume = tailor_resume(profile, job_desc)
    print("Resume generated")

    cover = generate_cover_letter(profile, job_desc)
    print("Cover letter generated")

    apply_job(job)

    print("Application attempted\n")