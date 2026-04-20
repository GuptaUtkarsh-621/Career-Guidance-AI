import streamlit as st
import os
import base64

# 1. PAGE CONFIG
st.set_page_config(page_title="Career Roadmap | Career Guidance AI", layout="wide")

# 2. VIVID BRANDING HELPERS
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
                background-color: rgba(10, 15, 30, 0.93); 
                z-index: -1;
            }}
            </style>
        ''', unsafe_allow_html=True)
    
    if os.path.exists("assets/style.css"):
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply Branding
apply_page_branding('logo.png')

# 3. CHECK LOGIN
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("⚠️ Please login from the main page first.")
    st.stop()

# 4. HEADER
st.markdown("""
    <div style='margin-bottom: 25px;'>
        <h1 style='margin-bottom: 0;'>🗺️ Personalized Career Roadmap</h1>
        <p style='color: #818CF8; font-weight: 600;'>Your Step-by-Step Journey to Industry Mastery</p>
    </div>
""", unsafe_allow_html=True)

# Roadmaps Data
roadmaps = {
    "Data Scientist": [
        {"Step": "Phase 1", "Goal": "Mathematics & Statistics", "Skills": "Linear Algebra, Calculus, Probability"},
        {"Step": "Phase 2", "Goal": "Programming Foundation", "Skills": "Python, Pandas, NumPy, Matplotlib"},
        {"Step": "Phase 3", "Goal": "Machine Learning", "Skills": "Scikit-Learn, Regression, Random Forest, Clustering"},
        {"Step": "Phase 4", "Goal": "Deep Learning & Big Data", "Skills": "TensorFlow, Spark, SQL"}
    ],
    "SDE": [
        {"Step": "Phase 1", "Goal": "DSA Fundamentals", "Skills": "Arrays, Linked Lists, Trees, Graphs, Sorting"},
        {"Step": "Phase 2", "Goal": "Core Development", "Skills": "System Design, OOPs, Database Management (DBMS)"},
        {"Step": "Phase 3", "Goal": "Frameworks", "Skills": "Django/Flask or SpringBoot/Node.js"},
        {"Step": "Phase 4", "Goal": "Deployment", "Skills": "Docker, Kubernetes, AWS/Azure"}
    ],
    "AI Engineer": [
        {"Step": "Phase 1", "Goal": "Advanced Python", "Skills": "FastAPI, Multithreading, Decorators"},
        {"Step": "Phase 2", "Goal": "MLOps", "Skills": "DVC, MLFlow, Pipeline Automation"},
        {"Step": "Phase 3", "Goal": "NLP & Vision", "Skills": "NLTK, OpenCV, HuggingFace Transformers"},
        {"Step": "Phase 4", "Goal": "Model Optimization", "Skills": "Quantization, ONNX, Edge AI"}
    ]
}

# 5. SELECTION CARD
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
selected_role = st.selectbox("🎯 Select your target career path:", list(roadmaps.keys()))
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. ROADMAP DISPLAY
if selected_role:
    st.markdown(f"### Learning Path: {selected_role}")
    
    # Wrap the timeline in a card
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    
    # Track completion for a progress bar
    completed_steps = 0
    total_steps = len(roadmaps[selected_role])
    
    for item in roadmaps[selected_role]:
        with st.expander(f"📍 {item['Step']}: {item['Goal']}"):
            st.markdown(f"""
                <div style='background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border-left: 4px solid #6366F1;'>
                    <p style='color: #CBD5E1; margin-bottom: 5px;'><strong>Key Skills to Master:</strong></p>
                    <p style='color: #818CF8;'>{item['Skills']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.checkbox("Mark as completed", key=f"{selected_role}_{item['Step']}"):
                completed_steps += 1

    # Show Progress
    st.markdown("---")
    progress_val = completed_steps / total_steps
    st.write(f"**Curriculum Progress: {int(progress_val*100)}%**")
    st.progress(progress_val)
    
    if progress_val == 1.0:
        st.success("🎉 Incredible! You've completed the roadmap. Time to apply for roles!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# 7. PRO-TIP CARD
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div class="premium-card" style="border-left: 5px solid #F59E0B; background: rgba(245, 158, 11, 0.05);">
        <p style="color: #F59E0B; font-weight: 700; margin-bottom: 5px;">💡 EXPERT GUIDANCE</p>
        <p style="color: #CBD5E1; font-size: 0.9rem;">Spend at least 4-6 weeks on each phase. Build 2 minor projects per phase to ensure the Random Forest engine detects your growth in the next assessment.</p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Developed by Utkarsh</div>', unsafe_allow_html=True)