Markdown
# 🎯 Career Guidance AI
**An Intelligent Career Navigation Ecosystem using Machine Learning & Generative AI**

---

## 🚀 Overview
Career Guidance AI is a high-performance counseling platform designed to bridge the gap between academic theory and industry reality. The system features a custom-built **Vivid Glassmorphism UI** and integrates multiple AI models to provide personalized career roadmaps, skill gap analysis, and interactive guidance.

## ✨ Key Features
- **Cognitive AI Assessment**: A 50-question diagnostic engine mapping psychological and technical traits to career domains (SDE, DS, MGMT, UX).
- **ML Career Predictor**: Utilizes a **Random Forest Classification** model to predict suitable roles based on academic and technical scores.
- **AI Voice Assistant**: A dual-interface (Voice/Text) assistant powered by **NLP** and **TTS** for real-time career support.
- **Skill Gap Analysis**: Interactive **Radar Intelligence** comparing user competencies against industry benchmarks.
- **Holographic Market Trends**: 2026 job market data visualization using 4D bubble charts (Salary vs. Difficulty vs. Demand).
- **Vivid Pro UI**: A modern Dark Mode interface featuring frosted glass containers, neon accents, and brand watermarking.

## 🛠️ Tech Stack
- **Frontend**: Streamlit (Python-based Framework)
- **Backend**: Python 3.10+
- **Machine Learning**: Scikit-Learn (Random Forest)
- **Generative AI**: Google Gemini 2.0 Flash API
- **Data Visualization**: Plotly (Holographic Charts)
- **Voice Intelligence**: SpeechRecognition & PyTTsx3
- **Database**: SQLite3 (Secure Authentication)
- **Styling**: Advanced CSS3 (Glassmorphism & Keyframe Animations)

## 📦 Installation & Setup

### 1. Prerequisites
Ensure Python 3.10+ is installed. Hardware requirements include a working microphone for the Voice Assistant module.

### 2. Setup Virtual Environment
```cmd
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
DOS
pip install -r requirements.txt
4. API & Secret Configuration
Create a .streamlit/secrets.toml file to securely store your AI credentials:

Ini, TOML
# .streamlit/secrets.toml
GEMINI_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY"
5. Launch System
DOS
streamlit run app.py
📂 Project Architecture
Plaintext
CareerGuidanceAI/
├── .streamlit/          # Secure API keys
├── assets/              # Vivid Dark CSS & Design Assets
├── pages/               # AI Assessment, Predictor, Trends, Assistant
├── utils/               # ML Models (Random Forest) & DB Management
├── app.py               # Central Portal Entry
├── logo.png             # Modern Project Identity
├── requirements.txt     # System Dependency List
└── README.md            # Technical Documentation
👤 Developer
Utkarsh Master of Computer Applications (MCA) Final Year Major Project

© 2026 Career Guidance AI | Secure AI Session Active


---

### 💡 Tips for your Final Viva/Presentation:

* **Mention "Modularity":** Explain to the external examiners that the project uses a **modular architecture** (separate `pages/` and `utils/`), which makes it easy to add more career paths or AI models in the future.
* **Highlight "Data Normalization":** In the Skill Gap Analysis, mention that you normalized user inputs against industry-standard benchmarks to ensure mathematical accuracy.
* **Explain the ML Choice:** If asked why you used **Random Forest** for the predictor, explain that it handles non-linear relationships between "Soft Skills" and "Technical Scores" better than simple linear models.



You now have a complete, professional project package. Good luck with your submission, Utkars