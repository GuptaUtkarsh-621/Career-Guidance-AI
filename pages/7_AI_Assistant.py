import streamlit as st
import speech_recognition as sr
import threading
import pyttsx3
import os
import base64
import time
from utils.processor import chatbot_response

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(page_title="Career AI Assistant", page_icon="🎙️", layout="centered")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def apply_page_branding(png_file):
    if os.path.exists(png_file):
        bin_str = get_base64(png_file)
        st.markdown(f'''
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{bin_str}");
                background-size: 400px;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            .stApp::before {{
                content: "";
                position: absolute;
                top: 0; left: 0; width: 100%; height: 100%;
                background-color: rgba(10, 15, 30, 0.94); 
                z-index: -1;
            }}
            /* Specific fix for chat avatars in dark mode */
            [data-testid="stChatMessageAvatarUser"] {{ background-color: #6366F1 !important; }}
            [data-testid="stChatMessageAvatarAssistant"] {{ background-color: #10B981 !important; }}
            </style>
        ''', unsafe_allow_html=True)
    
    if os.path.exists("assets/style.css"):
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

apply_page_branding('logo.png')

# AUTH CHECK
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("⚠️ Please login from the Home Page first.")
    st.stop()

# --- 2. SPEECH LOGIC (The Threaded Fix) ---
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        # Agar server pe hai toh sirf print karega, app band nahi hogi
        print("Audio output skipped: Local hardware not found.")
        st.warning("Voice output is only available when running locally.")
    def _speech_task():
        try:
            new_engine = pyttsx3.init()
            voices = new_engine.getProperty('voices')
            if len(voices) > 1:
                new_engine.setProperty('voice', voices[1].id)
            new_engine.setProperty('rate', 175) # Professional pace
            new_engine.say(text)
            new_engine.runAndWait()
            new_engine.stop()
        except Exception as e:
            print(f"Speech Error: {e}")
    threading.Thread(target=_speech_task, daemon=True).start()

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("🎙️ System Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        try:
            return r.recognize_google(audio)
        except Exception:
            return "ERROR: Could not capture audio clearly."

# --- 3. UI LAYOUT ---
st.markdown("""
    <div style='margin-bottom: 25px;'>
        <h1 style='margin-bottom: 0;'>🎙️ Career AI Assistant</h1>
        <p style='color: #818CF8; font-weight: 600;'>VOICE & TEXT COGNITIVE INTERFACE</p>
    </div>
""", unsafe_allow_html=True)

# Instructions Card
st.markdown("""
    <div class="premium-card" style="padding: 15px; border-left: 4px solid #6366F1; margin-bottom: 20px;">
        <p style="color: #CBD5E1; margin: 0; font-size: 0.9rem;">
            Welcome to the AI Control Hub. You can ask me about <strong>Roadmaps</strong>, 
            <strong>Skill Gaps</strong>, or specific <strong>Career Paths</strong>.
        </p>
    </div>
""", unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. CHAT HISTORY (Wrapped in Glass) ---
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. INPUT CONTROLS ---
st.markdown("<br>", unsafe_allow_html=True)
col_input, col_voice = st.columns([5, 1])

with col_input:
    prompt = st.chat_input("Enter your query here...")

with col_voice:
    # Stylized Voice Button
    voice_trigger = st.button("🎤 VOICE", use_container_width=True)

# --- 6. LOGIC ---
if voice_trigger:
    user_speech = get_voice_input()
    if "ERROR" not in user_speech:
        st.session_state.messages.append({"role": "user", "content": user_speech})
        response = chatbot_response(user_speech)
        st.session_state.messages.append({"role": "assistant", "content": response})
        speak(response)
        st.rerun()
    else:
        st.error(user_speech)

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = chatbot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    speak(response)
    st.rerun()

# Footer
st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Cognitive Assistant Module</div>', unsafe_allow_html=True)