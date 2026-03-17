import streamlit as st
import pandas as pd
import altair as alt
from utils.extractor import extract_text_from_pdf, extract_text_from_docx
from utils.ranker import rank_resumes
from utils.skills import extract_skills, extract_experience, extract_experience_years

# --- Streamlit UI ---
st.set_page_config(page_title="CV Ranker", layout="wide")
st.title(" CV Ranker Based on Job Description")
st.markdown("Upload a **Job Description** and multiple **Resumes**, and get an industry-level match score!")

# --- Upload JD ---
st.subheader("1. Upload Job Description")
jd_file = st.file_uploader("Upload JD (PDF or TXT)", type=["pdf","txt"])

# --- Upload Resumes ---
st.subheader("2. Upload Resumes")
resume_files = st.file_uploader(
    "Upload multiple Resumes (PDF or DOCX)",
    type=["pdf","docx"],
    accept_multiple_files=True
)

#  Rank Button
rank_trigger = st.button("🚀 Rank CVs", key="rank_button")

if rank_trigger and jd_file and resume_files:

    # Extract JD
    if jd_file.type == "application/pdf":
        jd_text = extract_text_from_pdf(jd_file)
    else:
        jd_text = jd_file.read().decode("utf-8")

    # Extract JD information
    jd_skills = extract_skills(jd_text)
    jd_exp = extract_experience(jd_text)
    jd_years = extract_experience_years(jd_text)

    # Resume storage
    resume_names = []
    resume_skills_list = []
    resume_exp_list = []
    resume_years_list = []

    for resume in resume_files:

        # Extract text
        if resume.type == "application/pdf":
            text = extract_text_from_pdf(resume)
        else:
            text = extract_text_from_docx(resume)

        # Skip if extraction failed
        if not text or not text.strip():
            continue

        # Add only valid resumes
        resume_names.append(resume.name)

        # Extract resume features
        resume_skills_list.append(extract_skills(text))
        resume_exp_list.append(extract_experience(text))
        resume_years_list.append(extract_experience_years(text))

    if len(resume_names) == 0:
        st.error("No valid resume text extracted.")
        st.stop()

    # Rank resumes
    with st.spinner("Ranking resumes..."):
        scores = rank_resumes(
            jd_skills,
            jd_exp,
            jd_years,
            resume_skills_list,
            resume_exp_list,
            resume_years_list
        )

    # Sort results
    ranked = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

    #create data for graph
    df = pd.DataFrame(ranked, columns=["Resume", "Score"])


    #completed Analyze
    st.success(f"{len(ranked)} resumes successfully analyzed!")
    # display
    st.subheader("Ranked Resumes")

    #bar
    chart = alt.Chart(df).mark_bar().encode(
        x="Score",
        y=alt.Y("Resume", sort="-x")
    )

    st.altair_chart(chart, use_container_width=True)
    
    
    for i, (name, score) in enumerate(ranked, 1):
        st.markdown(f"**{i}. {name}** — Match Score: `{score*100:.2f}%`")

elif rank_trigger:
    st.warning("Please upload both Job Description and Resumes.")