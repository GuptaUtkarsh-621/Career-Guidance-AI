import streamlit as st
import plotly.express as px
import pandas as pd
import os
import base64

# 1. PAGE CONFIG
st.set_page_config(page_title="Market Trends | Career Guidance AI", layout="wide")

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

# 3. AUTH CHECK
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("⚠️ Please login first.")
    st.stop()

# 4. HEADER
st.markdown("""
    <div style='margin-bottom: 25px;'>
        <h1 style='margin-bottom: 0;'>📈 2026 Job Market Insights</h1>
        <p style='color: #818CF8; font-weight: 600;'>AI-Driven Real-Time Economic Trends</p>
    </div>
""", unsafe_allow_html=True)

# 5. MARKET PULSE METRICS (Top Row)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.markdown('<div class="premium-card" style="padding:15px; text-align:center;">', unsafe_allow_html=True)
    st.metric("Top Growing Role", "AI Engineer", "+24%")
    st.markdown('</div>', unsafe_allow_html=True)
with col_m2:
    st.markdown('<div class="premium-card" style="padding:15px; text-align:center;">', unsafe_allow_html=True)
    st.metric("Avg Industry Salary", "14.5 LPA", "Lakhs/Year")
    st.markdown('</div>', unsafe_allow_html=True)
with col_m3:
    st.markdown('<div class="premium-card" style="padding:15px; text-align:center;">', unsafe_allow_html=True)
    st.metric("Highest Demand", "Full Stack Dev", "15k+ Openings")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. DATA PREP
data = {
    "Job Role": ["Data Scientist", "SDE", "AI Engineer", "Cybersecurity", "Cloud Architect", "Full Stack Dev"],
    "Avg Salary (LPA)": [15, 12, 18, 14, 16, 11],
    "Entry Difficulty (1-10)": [8, 6, 9, 7, 8, 5],
    "Job Openings": [5000, 12000, 4000, 6000, 5500, 15000]
}
df = pd.DataFrame(data)

# 7. HOLOGRAPHIC BUBBLE CHART
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
st.markdown("<h3 style='color: white;'>Market Analysis: Salary vs Difficulty</h3>", unsafe_allow_html=True)

fig = px.scatter(
    df, x="Entry Difficulty (1-10)", y="Avg Salary (LPA)",
    size="Job Openings", color="Job Role",
    hover_name="Job Role", size_max=65,
    template="plotly_dark",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Force transparency and neon grid
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="#cbd5e1"),
    xaxis=dict(gridcolor="#334155", title="Entry Difficulty (1-10)"),
    yaxis=dict(gridcolor="#334155", title="Avg Salary (LPA)"),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
)

st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 8. LEGEND & TIPS
st.markdown("<br>", unsafe_allow_html=True)
c_t1, c_t2 = st.columns(2)
with c_t1:
    st.markdown("""
        <div class="premium-card" style="height: 100%;">
            <h4 style="color: #818CF8;">📖 How to Read This</h4>
            <ul style="color: #CBD5E1; font-size: 0.9rem;">
                <li><strong>Vertical Axis:</strong> Higher bubbles mean better pay.</li>
                <li><strong>Horizontal Axis:</strong> Bubbles further right are harder roles.</li>
                <li><strong>Bubble Size:</strong> Large circles represent more hiring demand.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
with c_t2:
    st.markdown("""
        <div class="premium-card" style="height: 100%; border-left: 4px solid #10B981;">
            <h4 style="color: #10B981;">💡 Strategic Advice</h4>
            <p style="color: #CBD5E1; font-size: 0.9rem;">Targeting <strong>AI Engineering</strong> offers the highest return on investment, though entry difficulty is a 9. Combine with the Roadmap page to succeed.</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Market Insights Module</div>', unsafe_allow_html=True)