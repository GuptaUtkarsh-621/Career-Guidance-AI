import streamlit as st
import os
import base64
import time

# 1. PAGE CONFIG & VIVID BRANDING
st.set_page_config(page_title="Career Assessment | AI Evaluation", layout="centered")

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
            </style>
        ''', unsafe_allow_html=True)
    
    if os.path.exists("assets/style.css"):
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

apply_page_branding('logo.png')

# AUTH CHECK
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("⚠️ Access Denied. Please Login from the Home Page.")
    st.stop()

# 2. DATASET
questions = [
    # [Your 50 questions remain the same as provided]
    {"q": "Do you enjoy building logical structures like puzzles or algorithms?", "cat": "SDE"},
    {"q": "Are you interested in how Operating Systems manage memory?", "cat": "SDE"},
    {"q": "Would you prefer fixing a bug in code over designing a logo?", "cat": "SDE"},
    {"q": "Do you find satisfaction in optimizing code for speed?", "cat": "SDE"},
    {"q": "Does the idea of building a mobile app excite you?", "cat": "SDE"},
    {"q": "Do you like learning multiple programming languages?", "cat": "SDE"},
    {"q": "Are you interested in Backend infrastructure and APIs?", "cat": "SDE"},
    {"q": "Do you enjoy the process of rigorous software testing?", "cat": "SDE"},
    {"q": "Would you like to build your own compiler or game engine?", "cat": "SDE"},
    {"q": "Do you prefer working with Command Line Tools over GUIs?", "cat": "SDE"},
    {"q": "Are you interested in Cybersecurity and ethical hacking?", "cat": "SDE"},
    {"q": "Do you like automated tools that handle repetitive tasks?", "cat": "SDE"},
    {"q": "Does System Design and Architecture fascinate you?", "cat": "SDE"},
    {"q": "Do you enjoy Version Control systems like Git?", "cat": "SDE"},
    {"q": "Are you interested in Cloud Computing (AWS/Azure)?", "cat": "SDE"},
    {"q": "Do you enjoy analyzing patterns in large spreadsheets?", "cat": "DS"},
    {"q": "Is Probability and Statistics one of your favorite subjects?", "cat": "DS"},
    {"q": "Does the idea of teaching a machine to 'think' excite you?", "cat": "DS"},
    {"q": "Would you like to predict stock prices using historical data?", "cat": "DS"},
    {"q": "Do you enjoy data visualization and creating charts?", "cat": "DS"},
    {"q": "Are you interested in Neural Networks and Deep Learning?", "cat": "DS"},
    {"q": "Do you prefer SQL queries over UI designing?", "cat": "DS"},
    {"q": "Would you like to build a voice assistant like Alexa?", "cat": "DS"},
    {"q": "Do you enjoy cleaning and organizing messy information?", "cat": "DS"},
    {"q": "Are you curious about how Netflix recommends movies?", "cat": "DS"},
    {"q": "Do you like working with Python libraries like Pandas or NumPy?", "cat": "DS"},
    {"q": "Are you interested in Natural Language Processing (NLP)?", "cat": "DS"},
    {"q": "Do you enjoy research-oriented problem solving?", "cat": "DS"},
    {"q": "Does working with Big Data (Hadoop/Spark) interest you?", "cat": "DS"},
    {"q": "Do you prefer evidence-based decision making?", "cat": "DS"},
    {"q": "Do you like leading a team to achieve a common goal?", "cat": "MGMT"},
    {"q": "Are you good at resolving conflicts between people?", "cat": "MGMT"},
    {"q": "Do you enjoy planning timelines and project milestones?", "cat": "MGMT"},
    {"q": "Would you prefer being a Product Manager over a Developer?", "cat": "MGMT"},
    {"q": "Are you comfortable speaking in front of a large audience?", "cat": "MGMT"},
    {"q": "Do you enjoy resource management and budgeting?", "cat": "MGMT"},
    {"q": "Is 'Market Strategy' more interesting than 'Code Logic'?", "cat": "MGMT"},
    {"q": "Do you like talking to clients and gathering requirements?", "cat": "MGMT"},
    {"q": "Are you interested in Business Analytics?", "cat": "MGMT"},
    {"q": "Do you enjoy mentoring juniors or newcomers?", "cat": "MGMT"},
    {"q": "Do you notice when a button is 1 pixel off-center?", "cat": "UX"},
    {"q": "Do you enjoy choosing color palettes and themes?", "cat": "UX"},
    {"q": "Is the user's emotional experience a priority for you?", "cat": "UX"},
    {"q": "Do you enjoy sketching wireframes on paper?", "cat": "UX"},
    {"q": "Are you interested in Typography and Visual Hierarchy?", "cat": "UX"},
    {"q": "Would you rather use Figma than VS Code?", "cat": "UX"},
    {"q": "Do you enjoy making websites look beautiful and modern?", "cat": "UX"},
    {"q": "Do you like studying how users interact with apps?", "cat": "UX"},
    {"q": "Is accessibility (making apps for everyone) important to you?", "cat": "UX"},
    {"q": "Do you enjoy creative storytelling through visuals?", "cat": "UX"},
]

# 3. SESSION STATE
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
    st.session_state.results = {"SDE": 0, "DS": 0, "MGMT": 0, "UX": 0}
    st.session_state.finished = False

# 4. UI HEADER
st.markdown("""
    <div style='margin-bottom: 25px;'>
        <h1 style='margin-bottom: 0;'>🎯 AI Career Path Assessment</h1>
        <p style='color: #818CF8; font-weight: 600;'>COGNITIVE TRAIT EVALUATION ENGINE</p>
    </div>
""", unsafe_allow_html=True)

if not st.session_state.finished:
    # PROGRESS HUD
    st.markdown('<div class="premium-card" style="padding: 15px; margin-bottom: 20px;">', unsafe_allow_html=True)
    progress = st.session_state.q_idx / len(questions)
    st.write(f"**Assessment Progress: {int(progress*100)}%**")
    st.progress(progress)
    st.markdown(f"<p style='color:#94A3B8; font-size:12px;'>Question {st.session_state.q_idx + 1} of {len(questions)}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # QUESTION CARD
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    current_q = questions[st.session_state.q_idx]
    st.subheader(current_q['q'])
    
    ans = st.radio("Select your level of agreement:", 
                    ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                    index=None)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Confirm & Continue ➡️", use_container_width=True):
        if ans:
            weights = {"Strongly Disagree": 0, "Disagree": 1, "Neutral": 2, "Agree": 4, "Strongly Agree": 5}
            st.session_state.results[current_q['cat']] += weights[ans]
            
            if st.session_state.q_idx < len(questions) - 1:
                st.session_state.q_idx += 1
                st.rerun()
            else:
                st.session_state.finished = True
                st.rerun()
        else:
            st.error("Please provide an answer to proceed.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # 5. RESULTS DASHBOARD
    st.balloons()
    st.markdown('<div class="premium-card" style="border-left: 5px solid #10B981;">', unsafe_allow_html=True)
    st.header("🎊 Assessment Complete")
    
    res = st.session_state.results
    best_path = max(res, key=res.get)
    names = {"SDE": "Software Development Engineer", "DS": "Data Scientist / AI Engineer", 
             "MGMT": "Technical Product Manager", "UX": "UI/UX Designer"}

    st.success(f"### Recommended Specialization: **{names[best_path]}**")
    st.write("Our AI has mapped your traits to this domain with high affinity.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Visual Breakdown
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown("#### Your Domain Score Breakdown")
    for cat, score in res.items():
        max_possible = 75 if cat in ['SDE', 'DS'] else 50
        norm_score = min(score/max_possible, 1.0)
        
        st.write(f"**{names[cat]}**")
        st.progress(norm_score)
        st.markdown(f"<p style='color:#818CF8; font-size:12px; margin-top:-10px;'>Compatibility: {int(norm_score*100)}%</p>", unsafe_allow_html=True)
    
    if st.button("🔄 Retake AI Assessment", use_container_width=True):
        st.session_state.q_idx = 0
        st.session_state.results = {"SDE": 0, "DS": 0, "MGMT": 0, "UX": 0}
        st.session_state.finished = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer-note">© 2026 Career Guidance AI | Developed by Utkarsh</div>', unsafe_allow_html=True)