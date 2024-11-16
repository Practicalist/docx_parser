import streamlit as st
from docx import Document

# Title of the App
st.title("📄 Docx File Parser")

# Instructions
st.write("Upload a `.docx` file, and I will extract and display the text content for you.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a .docx file", type="docx")

# Handle file upload
if uploaded_file is not None:
    try:
        # Load the document
        doc = Document(uploaded_file)
        
        # Extract paragraphs
        extracted_text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text_area("Document Content", extracted_text, height=400)
        
        # Option to download extracted text as a .txt file
        st.download_button(
            label="📥 Download Extracted Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("Please upload a `.docx` file to begin.")

# Footer
st.write("---")
st.caption("Developed with ❤️ using Streamlit and Python.")
