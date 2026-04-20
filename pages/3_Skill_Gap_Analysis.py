import streamlit as st
import plotly.express as px
import pandas as pd
import os
import base64

# 1. PAGE CONFIG
st.set_page_config(page_title="Skill Gap Analysis | Career Guidance AI", layout="wide")

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

# Apply branding and watermark
apply_page_branding('logo.png')

# 3. HEADER
st.markdown("""
    <div style='margin-bottom: 25px;'>
        <h1 style='margin-bottom: 0;'>📊 Skill Gap Analysis</h1>
        <p style='color: #818CF8; font-weight: 600;'>Comparative Intelligence vs. Industry Benchmarks</p>
    </div>
""", unsafe_allow_html=True)

# 4. SKILL INPUTS (Wrapped in Premium Card)
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("<h3 style='color: white; margin-bottom:20px;'>Assess Your Competencies</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
industry_standards = {"Coding": 90, "Math": 80, "Logic": 85, "Comm": 75}

with col1:
    c_score = st.slider("Your Coding Score", 0, 100, 50, help="Programming and Scripting")
    m_score = st.slider("Your Math Score", 0, 100, 60, help="Quantitative Aptitude")

with col2:
    l_score = st.slider("Your Logic Score", 0, 100, 70, help="Problem Solving & Analytical")
    cm_score = st.slider("Your Comm Score", 0, 100, 80, help="Verbal & Written Communication")

user_skills = {"Coding": c_score, "Math": m_score, "Logic": l_score, "Comm": cm_score}
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. RADAR CHART (Styled for Dark Mode)
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("<h3 style='color: white; text-align: center;'>Industry Standard Comparison</h3>", unsafe_allow_html=True)

df = pd.DataFrame({
    'Skill': list(industry_standards.keys()) * 2,
    'Score': list(industry_standards.values()) + list(user_skills.values()),
    'Type': ['Standard'] * 4 + ['Your Level'] * 4
})

fig = px.line_polar(
    df, r='Score', theta='Skill', color='Type', 
    line_close=True,
    template="plotly_dark", # Use Dark Template
    color_discrete_map={"Standard": "#6366f1", "Your Level": "#10b981"} # Indigo vs Emerald
)

# Force background to be transparent to show the "Premium Card" and Watermark
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    polar=dict(
        bgcolor='rgba(15, 23, 42, 0.5)',
        radialaxis=dict(visible=True, range=[0, 100], gridcolor="#334155"),
        angularaxis=dict(gridcolor="#334155")
    ),
    font=dict(size=14, color="#cbd5e1"),
    legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5)
)

st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 6. PERSISTENT FOOTER
st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Developed by Utkarsh | Skills Analysis Engine</div>', unsafe_allow_html=True)