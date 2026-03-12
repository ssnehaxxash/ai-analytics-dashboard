import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

st.write("Upload a resume (PDF) to extract text.")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:

    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Resume Text")

    st.write(text[:2000])