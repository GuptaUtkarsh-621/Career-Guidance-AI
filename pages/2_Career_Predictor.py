import streamlit as st
from utils.processor import predict_career
import os
import base64

# 1. PAGE CONFIG (Only call this ONCE at the very top)
st.set_page_config(page_title="AI Predictor | Career Guidance AI", layout="wide")

# 2. VIVID BRANDING HELPERS
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def apply_page_branding(png_file):
    # Set Watermark
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
                background-color: rgba(10, 15, 30, 0.92); 
                z-index: -1;
            }}
            </style>
        ''', unsafe_allow_html=True)
    
    # Load CSS
    if os.path.exists("assets/style.css"):
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply Branding
apply_page_branding('logo.png')

# 3. SIDEBAR CTA
with st.sidebar:
    st.markdown("### Navigation")
    st.info("💡 Not sure about your exact skill levels?")
    if st.button("📝 Take 50-Question AI Test", use_container_width=True):
        st.switch_page("pages/6_AI_Assessment.py")
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state['logged_in'] = False
        st.switch_page("app.py")

# 4. MAIN CONTENT
# Check login status
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("⚠️ Please login from the main page first.")
    st.stop()

st.markdown("""
    <div style='margin-bottom: 25px;'>
        <h1 style='margin-bottom: 0;'>🤖 AI Career Path Analysis</h1>
        <p style='color: #818CF8; font-weight: 600;'>Powered by Random Forest Classification Engine</p>
    </div>
""", unsafe_allow_html=True)

# WRAP INPUTS IN PREMIUM CARD
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("<h3 style='color: white;'>Self-Assessment Input</h3>", unsafe_allow_html=True)
st.write("Adjust the sliders below to represent your current skill proficiency.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 📚 Academic & Technical")
    acad = st.slider("Academic Score (%)", 0, 100, 75, help="Your overall percentage in your degree.")
    code = st.slider("Coding & Scripting Skills", 0, 100, 60, help="Proficiency in Python, Java, C++, etc.")
    
with col2:
    st.markdown("#### 💬 Soft Skills")
    comm = st.slider("Communication Ability", 0, 100, 70, help="Public speaking and team collaboration.")
    logi = st.slider("Logical & Analytical Reasoning", 0, 100, 80, help="Problem solving and aptitude.")

st.markdown("<br>", unsafe_allow_html=True)
predict_btn = st.button("🚀 Generate Career Prediction", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. PREDICTION LOGIC & DYNAMIC RESULTS
if predict_btn:
    user_inputs = [acad, code, comm, logi]
    
    with st.spinner("AI is analyzing your profile..."):
        time.sleep(1) # Visual padding
        result, confidence = predict_career(user_inputs)
        
    # WRAP RESULT IN PREMIUM CARD
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="premium-card" style="border: 1px solid #10B981;">', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2 style='color: #10B981;'>Prediction Result: {result}</h2>
            <p style='color: #94A3B8;'>Our Random Forest model is highly confident in this path for you.</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric("AI Confidence", f"{round(confidence*100, 2)}%")
    with c2:
        st.markdown("<p style='margin-bottom:5px; font-size:12px; color:#94A3B8;'>PROBABILITY SCORE</p>", unsafe_allow_html=True)
        st.progress(confidence)
        
    st.balloons()
    st.info(f"✨ **Next Steps:** Based on your {round(confidence*100,1)}% match, we recommend checking the **{result} Roadmap** in the Generator section.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer Note
st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Developed by Utkarsh</div>', unsafe_allow_html=True)