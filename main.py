from src.agent.runner import run_agent
from src.db.init_db import init_db

with open("data/resume.txt", "r") as f:
    profile = f.read()

jobs = [
    "https://example.com",
    "https://google.com",
    "https://github.com"
]

if __name__ == "__main__":
    init_db()

    for job in jobs:
        run_agent(job, profile)