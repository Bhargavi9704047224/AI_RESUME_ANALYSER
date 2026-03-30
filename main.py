import streamlit as st
import PyPDF2
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# UI setup
st.set_page_config(page_title="AI Resume Critiquer", layout="centered")
st.title("AI Resume Critiquer 🚀")
st.write("Upload your resume and get AI-powered feedback")

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("API key not found. Check your .env file.")
    st.stop()

# Inputs
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "txt"])
job_role = st.text_input("Enter Job Role")
analyse = st.button("Analyze Resume")

# Extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        try:
            content = page.extract_text()
            if content:
                text += content + "\n"
        except:
            continue
    return text

# Extract text from file
def extract_text(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    return file.read().decode("utf-8", errors="ignore")

# Available working models (fallback system)
MODELS = [
    "llama-3.1-8b-instant",
    "llama3-8b-8192"
]

# Main logic
if analyse and uploaded_file:
    try:
        with st.spinner("Analyzing resume... 🔍"):

            resume_text = extract_text(uploaded_file)

            if not resume_text.strip():
                st.error("File has no readable content")
                st.stop()

            # Create client
            client = Groq(api_key=GROQ_API_KEY)

            # Prompt
            prompt = f"""
You are an expert ATS resume reviewer.

Analyze this resume for the role: {job_role}

Provide:
1. Resume Score out of 100
2. Strengths
3. Weaknesses
4. ATS Compatibility (Yes/No + reason)
5. Improvements (skills, keywords, formatting, projects)
6. Section-wise feedback
7. Final verdict (suitability + level)

Resume:
{resume_text}
"""

            # Try models one by one (fallback system)
            response = None
            for model in MODELS:
                try:
                    st.info(f"Trying model: {model}")

                    response = client.chat.completions.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": "You are an expert resume reviewer."},
                            {"role": "user", "content": prompt}
                        ]
                    )

                    st.success(f"Using model: {model}")
                    break

                except Exception as model_error:
                    st.warning(f"Model {model} failed. Trying next...")
                    continue

            if response is None:
                st.error("All models failed. Please check Groq API or try later.")
                st.stop()

            result = response.choices[0].message.content

            # Output
            st.subheader("📊 Analysis Result")
            st.markdown(result)

    except Exception as e:
        st.error(f"Error: {str(e)}")