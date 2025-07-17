import streamlit as st
import requests

st.title("📄 PDF Question Answering Chatbot")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question about the PDF")

if st.button("Get Answer") and uploaded_file and question:
    response = requests.post(
        "http://localhost:8000/query",
        files={"file": uploaded_file},
        data={"question": question}
    )
    st.success(response.json().get("answer"))
