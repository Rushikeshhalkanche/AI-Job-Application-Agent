from src.llm.llm_client import ask_llm

def infer_field(field, context):
    prompt = f"""
Answer this job application field professionally.

Field:
{field}

Candidate Info:
{context}
"""
    return ask_llm(prompt)
