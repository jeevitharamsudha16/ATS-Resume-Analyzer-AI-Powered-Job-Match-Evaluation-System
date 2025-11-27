from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai


# ==============================
# CONFIGURE GEMINI API
# ==============================
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# ==============================
# GEMINI RESPONSE FUNCTION
# ==============================
def get_gemini_response(prompt, pdf_content, job_description):
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
        [
            prompt,
            pdf_content[0],   # 1st PDF page image
            job_description
        ]
    )
    return response.text


# ==============================
# PDF → IMAGE CONVERSION
# ==============================
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        uploaded_file.seek(0)  # Reset file pointer

        # Convert PDF to images using poppler
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # Convert image → JPEG bytes
        img_bytes = io.BytesIO()
        first_page.save(img_bytes, format="JPEG")
        img_bytes = img_bytes.getvalue()

        # Create Base64 payload for Gemini
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_bytes).decode()
            }
        ]
        return pdf_parts

    else:
        raise FileNotFoundError("No file uploaded")


# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

job_description = st.text_area("Job Description:", key="input")

uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

# Buttons
submit_analyze = st.button("Tell Me About the Resume")
submit_match = st.button("Percentage Match")


# ==============================
# PROMPTS
# ==============================
prompt_analysis = """
You are an experienced Technical Human Resource Manager.
Your task is to review the provided resume against the job description.
Provide a professional evaluation on:
1. Whether the candidate's profile aligns with the role.
2. Strengths of the applicant.
3. Weaknesses of the applicant.
4. Missing skills or gaps vs job description.
"""

prompt_match = """
You are a skilled ATS (Applicant Tracking System) scanner.
Evaluate the resume against the job description and provide:

1. Percentage match (only number first).
2. Missing keywords.
3. Final thoughts or recommendations.

Be strict and realistic.
"""


# ==============================
# SUBMISSION HANDLING
# ==============================
if submit_analyze:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(prompt_analysis, pdf_content, job_description)
        st.subheader("Analysis Result")
        st.write(response)
    else:
        st.error("Please upload a PDF resume.")

elif submit_match:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(prompt_match, pdf_content, job_description)
        st.subheader("ATS Match Result")
        st.write(response)
    else:
        st.error("Please upload a PDF resume.")
