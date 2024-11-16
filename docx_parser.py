import streamlit as st
from docx import Document

st.title("Upload Your .docx File")
uploaded_file = st.file_uploader("Choose a .docx file", type="docx")

if uploaded_file:
    doc = Document(uploaded_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    st.write("Extracted Text:")
    st.text(text)
