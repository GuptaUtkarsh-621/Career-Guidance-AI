import streamlit as st
from utils.processor import extract_text_from_pdf, analyze_resume_with_ai
import os

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Dashboard | Career Guidance AI", layout="wide")

# 2. LOAD EXTERNAL CSS
if os.path.exists("assets/style.css"):
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 3. GLOBAL BRANDING (Watermark & Footer)
st.markdown('<div class="watermark">CAREER GUIDANCE AI</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="footer-note">
        © 2026 Career Guidance AI | Developed by Utkarsh | MCA Major Project
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR BRANDING
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.markdown("### Career Guidance AI")
st.sidebar.markdown(f"**User:** {st.session_state.get('username', 'Guest')}")
st.sidebar.markdown("---")

# 5. DASHBOARD HEADER
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;'>
        <div>
            <h1 style='color: #FFFFFF; margin-bottom: 0;'>Personal Dashboard</h1>
            <p style='color: #94A3B8;'>Welcome back! Here is your latest career intelligence.</p>
        </div>
        <div style='background: rgba(99, 102, 241, 0.2); color: #818CF8; padding: 10px 20px; border-radius: 12px; font-weight: 600; border: 1px solid rgba(99, 102, 241, 0.3);'>
            ✨ AI Assistant Online
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. TOP METRIC CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="premium-card">
            <p class="metric-title">Lessons Completed</p>
            <h1 class="metric-value">46</h1>
            <p style="color: #F59E0B; font-size: 13px; margin-top:8px;">▼ 7% vs last month</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="premium-card">
            <p class="metric-title">Skill Tracker</p>
            <h1 class="metric-value">127h</h1>
            <p style="color: #10B981; font-size: 13px; margin-top:8px;">▲ 12% total growth</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="premium-card">
            <p class="metric-title">Job Matches</p>
            <h1 class="metric-value">12</h1>
            <p style="color: #6366F1; font-size: 13px; margin-top:8px;">New roles identified</p>
        </div>
    """, unsafe_allow_html=True)

# 7. BOTTOM SECTION: SKILLS & CV UPLOAD
col_left, col_right = st.columns([2, 1.2])

with col_left:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom: 25px; color: white;'>Skill Proficiency</h3>", unsafe_allow_html=True)
    
    # Helper for Skill Bars
    def render_skill(name, percentage, color):
        st.markdown(f"""
            <div class="skill-container">
                <div class="skill-label-row">
                    <span class="skill-label" style="color: #CBD5E1;">{name}</span>
                    <span style="color: #94A3B8; font-size: 13px;">{percentage}%</span>
                </div>
                <div class="progress-bg">
                    <div class="progress-fill" style="width: {percentage}%; background-color: {color}; box-shadow: 0 0 10px {color}66;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    render_skill("Python & Backend", 85, "#6366F1")
    render_skill("Data Science / ML", 72, "#A855F7")
    render_skill("UI/UX & Frontend", 91, "#10B981")
    render_skill("Database (SQL/SQLite)", 60, "#F59E0B")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<p class="metric-title" style="text-align: center;">AI Resume Parser</p>', unsafe_allow_html=True)
    
    # Real Working File Uploader
    uploaded_file = st.file_uploader(
        "Upload Resume", 
        type=['pdf'], 
        key="dash_cv_upload", 
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        st.success(f"📄 {uploaded_file.name} ready")
        
        if st.button("🔍 Analyze with Gemini", use_container_width=True):
            with st.spinner("AI is parsing your credentials..."):
                try:
                    resume_text = extract_text_from_pdf(uploaded_file)
                    analysis = analyze_resume_with_ai(resume_text)
                    st.markdown("---")
                    st.markdown(f"<div style='font-size: 0.9rem; color: #CBD5E1;'>{analysis}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Analysis failed: {e}")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Career Prediction", use_container_width=True):
        st.switch_page("pages/2_Career_Predictor.py")
    
    st.markdown('</div>', unsafe_allow_html=True)