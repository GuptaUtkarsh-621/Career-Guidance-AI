import streamlit as st
from google import genai
import joblib
import numpy as np
import pyttsx3
import threading
import PyPDF2
import io

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to let Gemini analyze the Resume
def analyze_resume_with_ai(resume_text):
    from google import genai
    import streamlit as st
    
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        # KEY FIX 1: Truncate text to keep token count low (avoids 429 error)
        short_text = resume_text[:1500] 
        
        # KEY FIX 2: Use the exact model string 'gemini-2.0-flash' 
        # (The library adds the 'models/' part automatically)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Analyze this resume briefly. List: 1. Main Skills, 2. Best Role. Text: {short_text}"
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ **Quota reached.** Please wait 60 seconds."
        elif "404" in str(e):
            return "❌ **Model Error:** The AI model name was not recognized. Ensure you are using 'gemini-2.0-flash'."
        return f"AI Analysis failed: {e}"
# --- 1. AI CAREER PREDICTION (Random Forest) ---
def predict_career(input_data: list):
    try:
        model = joblib.load('models/random_forest_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        data_scaled = scaler.transform(np.array([input_data]))
        prediction = model.predict(data_scaled)
        probs = model.predict_proba(data_scaled)
        return prediction[0], np.max(probs)
    except Exception as e:
        return f"Error: {e}", 0.0

# --- 2. CHATBOT LOGIC (Hybrid: Local + Gemini) ---
def chatbot_response(query):
    query = query.lower()
    
    # --- 1. LOCAL KNOWLEDGE BASE (Instant & No Quota Required) ---
    # This ensures common questions always get an answer
    knowledge_base = {
        "ai": "Artificial Intelligence is the simulation of human intelligence by machines, especially computer systems.",
        "data science": "Data Science involves extracting insights from structured and unstructured data using scientific methods and algorithms.",
        "data engineer": "Data Engineers build the infrastructure (pipelines) that allows data to flow from source to analysts.",
        "machine learning": "Machine Learning is a subset of AI that focuses on building systems that learn from data to improve accuracy.",
        "roadmap": "You can find step-by-step learning paths in our 'Roadmap Generator' section.",
        "mca": "Master of Computer Applications (MCA) is a professional master's degree in computer science.",
        "python": "Python is the primary language for AI and Data Science due to its extensive library support like NumPy and Pandas."
    }

    # Check if any keyword exists in the user query
    for key in knowledge_base:
        if key in query:
            return knowledge_base[key]

    # --- 2. GEMINI AI FALLBACK (For everything else) ---
    try:
        from google import genai
        import streamlit as st
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Answer this career-related question briefly: {query}"
        )
        return response.text

    except Exception as e:
        if "429" in str(e):
            return ("⏳ **API Limit Reached.** Since I'm using the Free Tier, "
                    "please wait 30-60 seconds before asking another non-technical question.")
        return "I am currently learning more about that. Please ask about Data Science or AI!"

# --- 3. VOICE ASSISTANT (TTS) ---
def speak(text):
    def _speech_task():
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except:
            pass
    threading.Thread(target=_speech_task, daemon=True).start()