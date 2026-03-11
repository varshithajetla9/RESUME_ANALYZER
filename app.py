import streamlit as st
import pdfplumber

st.title("Resume Analyzer")

# Skills to check
skills = ["python","sql","machine learning","data analysis",
          "deep learning","excel","power bi","tableau","communication"]

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text.lower()

if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text[:1000])

    st.subheader("Skill Analysis")

    found_skills = []
    score = 0

    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)
            score += 10

    st.write("Skills Found:")
    st.write(found_skills)

    st.subheader("Resume Score")
    st.progress(score)

    st.write(f"Your Resume Score: {score} / 100")

    if score >= 70:
        st.success("Strong Resume")
    elif score >= 40:
        st.warning("Resume can be improved")
    else:
        st.error("Add more relevant skills")