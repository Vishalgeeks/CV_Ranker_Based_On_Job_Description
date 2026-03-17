# AI Resume / CV Ranker

An AI-powered resume screening system that automatically ranks candidate resumes against a job description using semantic similarity and weighted scoring.

This project extracts skills and experience from resumes and compares them with job requirements using transformer-based embeddings to identify the most relevant candidates.

---

# Project Overview

Recruiters often receive hundreds of resumes for a single job role. Manually reviewing them is time-consuming and inefficient.

This project implements an **AI-based resume ranking system** that:

• Extracts important information from resumes
• Compares candidates with a job description
• Calculates a relevance score
• Ranks candidates automatically

The system uses **semantic similarity with transformer embeddings** to understand contextual relationships between skills and experience.

Example:

Job Description:
Machine Learning

Resume Skills:
TensorFlow, PyTorch

The system detects the **semantic relationship** between them and produces a meaningful similarity score.

---

# Features

• Resume parsing from **PDF and DOCX files**
• Job Description parsing from **PDF or TXT**
• Automatic **skill extraction**
• **Experience extraction and duration estimation**
• Semantic similarity matching using transformer embeddings
• Weighted scoring based on multiple candidate attributes
• Automatic **candidate ranking system**
• Interactive **visualization dashboard**

---

# Tech Stack

This project is built using:

• Python
• Streamlit – Web interface
• SentenceTransformers – Semantic embeddings
• scikit-learn – Cosine similarity computation
• PDF/DOCX parsing libraries for document processing

---

# Project Structure

```
project/
│
├── main.py
│   Streamlit application (UI and workflow)
│
├── utils/
│   ├── extractor.py
│   │   PDF and DOCX text extraction
│   │
│   ├── skills.py
│   │   Skill and experience extraction logic
│   │
│   └── ranker.py
│       Resume ranking and scoring algorithm
│
├── requirements.txt
│   Project dependencies
│
└── README.md
    Project documentation
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ai-resume-ranker.git
cd ai-resume-ranker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the Streamlit app:

```bash
streamlit run main.py
```

The application will open in your browser.

---

# Usage

1. Upload a **Job Description (PDF or TXT)**
2. Upload multiple **Resumes (PDF or DOCX)**
3. Click **Rank CVs**
4. The system will analyze and rank candidates automatically

Output includes:

• Match percentage for each resume
• Ranked candidate list
• Visualization dashboard

---

# System Pipeline

Job Description Upload
↓
JD Text Extraction
↓
JD Skill + Experience Extraction
↓
Resume Upload
↓
Resume Text Extraction
↓
Resume Feature Extraction
↓
Semantic Embedding Generation
↓
Cosine Similarity Matching
↓
Weighted Scoring Algorithm
↓
Resume Ranking
↓
Visualization Dashboard
↓
Final Ranked Candidate List

---

# Ranking Algorithm

Each resume receives a final score based on weighted factors:

Skill Match → 50%
Experience Match → 30%
Experience Duration → 20%

Final Score Formula:

```
Score =
0.5 × Skill Similarity
+ 0.3 × Experience Similarity
+ 0.2 × Experience Duration Score
```

Resumes are sorted by the final score to identify the best candidates.

---

# Visualization

The application generates a **horizontal bar chart** showing the ranking of all uploaded resumes based on their match scores.

This helps recruiters quickly identify the strongest candidates.

---

# Example Output

1. Resume_A.pdf — 82%
2. Resume_B.pdf — 67%
3. Resume_C.pdf — 54%

---

# Future Improvements

• Skill gap analysis between candidate and job description
• Resume clustering based on job domains
• Integration with Applicant Tracking Systems (ATS)
• Advanced NLP-based information extraction
• Multi-job ranking support

---


