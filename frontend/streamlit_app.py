import streamlit as st
import requests

st.set_page_config(
    page_title="Document Extractor",
    layout="centered"
)

st.title(
    "Intelligent Document Extraction Platform"
)

st.write(
    "Upload your document for extraction"
)

document_type = st.selectbox(
    "Select Document Type",
    [
        "aadhaar",
        "passport",
        "license",
        "invoice"
    ]
)

uploaded_file = st.file_uploader(
    "Upload File",
    type=["png", "jpg", "jpeg", "pdf"]
)

if st.button("Extract Data"):

    if uploaded_file:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue()
            )
        }

        data = {
            "document_type": document_type
        }

        response = requests.post(
            "http://localhost:8000/extract",
            files=files,
            data=data
        )

        if response.status_code == 200:

            st.success(
                "Extraction Successful"
            )

            st.json(response.json())

        else:

            st.error(
                response.text
            )