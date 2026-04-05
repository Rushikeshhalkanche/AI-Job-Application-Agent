# 🤖 AI Job Application Agent

An end-to-end **Agentic AI system** that automates the job application workflow.
The system processes job URLs, generates tailored resumes and cover letters, detects ATS platforms, and simulates application submission using browser automation.

---

## 🚀 Objective

This project demonstrates the ability to design and build a **real-world AI workflow** that integrates:

* LLM-based content generation
* Agent orchestration
* Browser automation
* Structured system design

---

## ⚙️ Features

✅ Resume Tailoring using LLM (Groq)
✅ Cover Letter Generation
✅ ATS Detection (Workday, Greenhouse, Lever)
✅ Browser Automation using Playwright
✅ Sequential Job Processing (Agent Pipeline)
✅ Modular & Extensible Architecture

---

## 🧠 System Workflow

1. Job URLs are added to a queue
2. The agent processes jobs one by one
3. Detects ATS platform from URL
4. Generates:

   * Tailored Resume
   * Cover Letter
5. Opens browser using Playwright
6. Attempts to fill application form
7. Moves to next job

---

## 🏗️ Project Structure

```
job_application_agent/
│
├── data/
│   └── resume.txt
│
├── src/
│   ├── agent/
│   │   └── runner.py
│   │
│   ├── llm/
│   │   ├── llm_client.py
│   │   ├── resume.py
│   │   ├── cover_letter.py
│   │   └── field_infer.py
│   │
│   ├── ats/
│   │   └── detector.py
│   │
│   ├── browser/
│   │   └── apply.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Groq API (LLM)
* Playwright (Browser Automation)
* SQLite (optional DB)
* dotenv

---

## 🔑 Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd job_application_agent
```

---

### 2. Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
playwright install
```

---

### 4. Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Add Resume Data

Create:

```
data/resume.txt
```

Add your profile details (skills, experience, projects).

---

### 6. Run the Agent

```
python main.py
```

---

## 🧪 Demo Behavior

* Agent processes multiple job URLs sequentially
* Generates resume & cover letter for each job
* Opens browser and simulates application flow

⚠️ For demo purposes, placeholder URLs are used.
The system is designed to work with real ATS platforms.

---

## 🔍 ATS Detection

The system supports detection of:

* Workday
* Greenhouse
* Lever

Based on URL patterns.

---

## ⚠️ Limitations

* Dynamic ATS forms require platform-specific selectors
* Authentication (login) is not handled
* Form filling is partially simulated
* Placeholder URLs used for stable demo

---

## 🚀 Future Improvements

* Human-in-the-loop (HITL) for unknown fields
* Intelligent DOM-based field detection
* Resume parsing from PDF
* Multi-agent parallel job processing
* Integration with real ATS platforms

---

## 💡 Key Highlights

* Designed as an **Agentic AI system**, not just a script
* Modular and scalable architecture
* Model-agnostic (can switch between Groq, OpenAI, Ollama)


