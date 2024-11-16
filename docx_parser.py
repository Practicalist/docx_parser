import streamlit as st
from docx import Document

st.title("Test python-docx")

try:
    doc = Document()
    st.write("python-docx imported and working correctly!")
except Exception as e:
    st.error(f"Error: {e}")
