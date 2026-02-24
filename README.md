# 🎯 AI Career Advisor (Production-Level)

A production-ready AI Career Advisor chatbot built using **Google Gemini API**, **Streamlit**, and multi-turn conversational memory.

This system provides structured career guidance including skill gap analysis, learning roadmaps, and internship strategies.

---

## 🚀 Features

- ✅ Gemini API Integration  
- ✅ Multi-turn conversational memory  
- ✅ Advanced prompt engineering  
- ✅ Structured career guidance format  
- ✅ Clean Streamlit UI  
- ✅ Modular project architecture  
- ✅ Production-ready code structure  

---

## 🧠 How It Works

The chatbot uses:

- System-level prompt engineering to restrict domain
- Structured output formatting
- Gemini conversational session for memory handling
- Exception handling for API rate limits

The bot responds using this structured format:

- 🎯 Career Goal  
- 🛠 Current Skills  
- ❌ Skill Gaps  
- 📚 Learning Roadmap  
- 🚀 Internship Strategy  

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- Git & GitHub

---

## 📦 Project Structure

```
career_advisor/
│
├── app.py
├── prompts.py
├── requirements.txt
├── .gitignore
└── services/
    └── gemini_service.py
```

---

## 🔑 Setup Instructions (Local)

1. Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/ai-career-advisor.git
```

2. Navigate to project folder:
```
cd ai-career-advisor
```

3. Create virtual environment:
```
python -m venv venv
```

4. Activate environment:
```
venv\Scripts\activate
```

5. Install dependencies:
```
pip install -r requirements.txt
```

6. Create a `.env` file and add:
```
gemini_key=YOUR_API_KEY
```

7. Run application:
```
streamlit run app.py
```

---

## 🌍 Deployment

The application is designed for deployment on AWS EC2 with public accessibility.

---

## 📌 Author

Mohammed Ashwaq  
Aspiring Data & AI Professional  

---

## ⚠ Note

This project is built for educational and portfolio demonstration purposes.
