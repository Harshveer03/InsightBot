import streamlit as st
import requests
from PIL import Image
import os

st.set_page_config(page_title="InsightBot", layout="centered")
st.title("🤖 InsightBot")
st.markdown("Upload a **PDF or image** and ask a question about its content.")

backend_url = "http://localhost:5000/upload"

uploaded_file = st.file_uploader("Upload PDF or Image", type=["pdf", "jpg", "jpeg", "png"])
question = st.text_input("Ask a question about the content:")

if uploaded_file:
    file_ext = uploaded_file.name.split('.')[-1].lower()
    
    st.subheader("📄 File Preview")
    if file_ext in ["jpg", "jpeg", "png"]:
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name, use_column_width=True)
    elif file_ext == "pdf":
        st.write(f"Uploaded PDF: **{uploaded_file.name}**")

if st.button("Get Answer"):
    if uploaded_file and question:
        with st.spinner("Processing..."):
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            data = {"question": question}
            try:
                response = requests.post(backend_url, files=files, data=data)
                response_data = response.json()
                if "answer" in response_data:
                    st.success(response_data["answer"])
                else:
                    st.error(f"Error: {response_data.get('error', 'Unknown error')}")
            except Exception as e:
                st.error(f"Exception: {e}")
    else:
        st.warning("Please upload a file and enter a question.")
