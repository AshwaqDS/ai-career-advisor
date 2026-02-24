import os
import streamlit as st
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT
from services.gemini_service import GeminiService


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎯",
    layout="wide"
)


# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("gemini_key")

if not api_key:
    st.error("⚠️ Gemini API key not found. Check your .env file.")
    st.stop()


# -----------------------------
# Initialize Gemini Service
# -----------------------------
if "gemini_service" not in st.session_state:
    service = GeminiService(api_key)
    service.start_chat(SYSTEM_PROMPT)
    st.session_state.gemini_service = service

service = st.session_state.gemini_service


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("📌 About This Project")
    st.write("""
    AI Career Advisor – Production Level

    ✔ Gemini API Integration  
    ✔ Multi-turn Memory  
    ✔ Advanced Prompt Engineering  
    ✔ Clean Streamlit UI  

    Ask career-related questions only.
    """)

    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = []
        service.start_chat(SYSTEM_PROMPT)
        st.success("Conversation Reset")


# -----------------------------
# Main UI
# -----------------------------
st.title("🎯 AI Career Advisor")
st.markdown("""
I help with:
- Career planning  
- Skill gap analysis  
- Learning roadmap  
- Internship & job preparation  

💡 Ask any career-related question.
""")


# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display Chat Messages
# -----------------------------
for role, text in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(text)


# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Type your career-related question here...")

if user_input:

    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        with st.spinner("Analyzing your career path..."):
            response = service.send_message(user_input)

    except Exception as e:
        if "429" in str(e):
            response = "⚠️ API quota exceeded. Please try again later."
        else:
            response = "⚠️ Service temporarily unavailable. Please try again."

    st.session_state.messages.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)