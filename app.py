import streamlit as st
from utils.db_manager import create_usertable, add_userdata, login_user
import time
import os
import base64

# 1. SET PAGE CONFIG
st.set_page_config(page_title="Career Guidance AI | Portal", page_icon="🎯", layout="centered")

# 2. HELPER FOR WATERMARK
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_watermark(png_file):
    if os.path.exists(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: 450px;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(10, 15, 30, 0.94); /* Dims the logo to make it a watermark */
            z-index: -1;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

# 3. LOAD CSS
if os.path.exists("assets/style.css"):
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    create_usertable()
    
    # Apply Image Watermark
    set_watermark('logo.png')
    
    # Persistent Footer
    st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Developed by Utkarsh | MCA Project</div>', unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        # LOGIN VIEW
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown("""
            <div style='text-align: center; margin-bottom: 20px;'>
                <h1 style='margin-bottom: 0;'>Career Guidance AI</h1>
                <p style='color: #818CF8; font-weight: 600; letter-spacing: 2px;'>NAVIGATING YOUR FUTURE</p>
            </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 Access Portal", "📝 Register Account"])
        with tab1:
            with st.form("login_form"):
                user = st.text_input("Username", placeholder="Enter username")
                pswd = st.text_input("Password", type='password', placeholder="••••••••")
                if st.form_submit_button("Launch Dashboard →", use_container_width=True):
                    if login_user(user, pswd):
                        st.session_state.update({'logged_in': True, 'username': user})
                        st.balloons()
                        st.rerun()
                    else:
                        st.error("Invalid Credentials")
        
        with tab2:
            with st.form("signup_form"):
                new_user = st.text_input("Choose Username")
                new_pswd = st.text_input("Choose Password", type='password')
                if st.form_submit_button("Initialize Account", use_container_width=True):
                    add_userdata(new_user, new_pswd)
                    st.success("Account Created! Please Sign In.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        # LOGGED IN VIEW - DASHBOARD HEADER
        st.markdown("""
            <div style='background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; 
                        border: 1px solid rgba(129, 140, 248, 0.3); margin-bottom: 25px; text-align: center;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.3);'>
                <h1 style='margin: 0; font-size: 2.8rem; background: linear-gradient(90deg, #818CF8, #C084FC);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                           text-shadow: 2px 2px 4px rgba(0,0,0,0.2); font-family: "Segoe UI", Roboto, sans-serif;'>
                    🚀 Career Guidance AI System
                </h1>
                <p style='margin: 10px 0 0 0; color: #818CF8; font-size: 0.9rem; letter-spacing: 4px; font-weight: 600;'>
                    INTELLIGENT CAREER NAVIGATOR
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown(f"""
            <div style='text-align: center;'>
                <h2 style='margin-bottom: 0;'>Welcome Back, {st.session_state['username']}!</h2>
                <p style='color: #10B981; font-weight: 600;'>AI Systems Ready • Session Secure</p>
            </div>
        """, unsafe_allow_html=True)
        
        col_nav, col_logout = st.columns([3, 1.2])
        with col_nav:
            st.info("💡 **Navigation:** Use the Sidebar to access the AI Predictor and Analysis modules.")
        with col_logout:
            if st.button("Logout", use_container_width=True):
                st.session_state['logged_in'] = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # FEATURE HIGHLIGHTS
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🛠️ Core AI Capabilities")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="premium-card" style="padding:20px; text-align:center; height:180px;"><h3>📊 Analytics</h3><p style="font-size:0.8rem; color:#94A3B8;">ML skill gap analysis.</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="premium-card" style="padding:20px; text-align:center; height:180px;"><h3>🤖 AI Guide</h3><p style="font-size:0.8rem; color:#94A3B8;">Gemini-powered CV parsing.</p></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="premium-card" style="padding:20px; text-align:center; height:180px;"><h3>🗺️ Roadmaps</h3><p style="font-size:0.8rem; color:#94A3B8;">Interactive career guidance.</p></div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()