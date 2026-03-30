# 🚀 AI Resume Critiquer

An AI-powered web application that analyzes resumes and provides detailed feedback using LLMs.

## 📌 Features

- 📄 Upload resume (PDF / TXT)
- 🤖 AI-based resume analysis
- 📊 Resume score (out of 100)
- ✅ Strengths & ❌ Weaknesses
- 🎯 ATS compatibility check
- 🛠 Suggestions for improvement
- 📋 Section-wise feedback
- 💼 Role-based evaluation

## 🛠 Tech Stack

- Python
- Streamlit
- PyPDF2
- Groq API (LLM)
- python-dotenv

## 📂 Project Structure

AI-Resume-Critiquer/
│
├── app.py
├── requirements.txt
├── .env
└── README.md

## ⚙️ Setup Instructions



1 Create virtual environment  
python -m venv venv  
venv\Scripts\activate  

2 Install dependencies  
pip install -r requirements.txt  

3 Add API Key  
Create a `.env` file:  
GROQ_API_KEY=your_api_key_here  

4 Run the app  
python -m streamlit run main.py  

## 📊 How It Works

1. User uploads resume  
2. Text is extracted using PyPDF2  
3. Resume is sent to Groq LLM  
4. AI analyzes and returns feedback  
5. Results displayed in Streamlit UI  

## 🚀 Future Improvements

- 📈 Resume vs Job Match %
- 📊 Score visualization (progress bar)
- 🧠 Skill gap detection
- 📄 Downloadable report
- 🌐 Deployment

## ⚠️ Important Notes

- Do NOT share your `.env` file  
- Add `.env` to `.gitignore  

## 👩‍💻 Author

Bhargavi
Interested in AI, Data Science, and ML  
