import streamlit as st
import database as db

# Initialize the database (this is good practice to have here)
db.init_db()

# Page Configuration
st.set_page_config(
    page_title="Resume Checker: PlacementIQ",
    page_icon="💼",
    layout="wide"
)

# Load Custom CSS
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file '{file_name}' not found. Please make sure it's in the same folder as Home.py.")

# Load the CSS file
load_css("style.css")


# --- HOME PAGE CONTENT ---
st.title("Resume Checker: PlacementIQ 💼")
st.header("Your intelligent assistant for talent acquisition, powered by PlacementIQ.")

# st.markdown(
#     '''<div class="main-content-text">
#     This powerful tool is designed to be <b>robust, scalable, and flexible</b>, helping your placement team handle thousands of resumes efficiently.<br><br>
#     <b>Project Objectives:</b><br>
#     <ul>
#         <li><b>Automate</b> resume evaluation against job requirements at scale.</li>
#         <li><b>Generate</b> a Relevance Score (0–100) for each resume.</li>
#         <li><b>Highlight</b> missing skills, certifications, or projects.</li>
#         <li><b>Provide</b> a clear verdict (High / Medium / Low suitability) to recruiters.</li>
#         <li><b>Offer</b> personalized improvement feedback to students.</li>
#     </ul>
#     <hr>
#     <b>How to Use This App:</b>
#     <ol>
#         <li><b>Open the Sidebar:</b> Click the <code>&gt;</code> arrow in the top-left corner.</li>
#         <li><b>Navigate:</b> Select the page you want to visit, like <b>'Resume Checker'</b> or <b>'Dashboard &amp; History'</b>.</li>
#         <li><b>Direct to Resume Checker:</b> Or, use the button below to go directly to the Resume Checker page.</li>
#     </ol>
#     </div>''', unsafe_allow_html=True)


st.markdown("""
Welcome to *Resume Checker Hire Wise*! This tool is your intelligent assistant for streamlining the recruitment process. It's built to be robust, scalable, and flexible, empowering your team to find the best candidates faster.

### Key Features
* *🤖 Automated AI Analysis:* Instantly score resumes against job descriptions to eliminate manual screening.
* *💯 Data-Driven Scoring:* Get a clear relevance score from 0-100 for every candidate.
* *🎯 Skill Gap Identification:* Automatically highlight missing keywords and qualifications.
* *✅ Quick Verdicts:* Receive an immediate verdict (High, Medium, or Low Fit) to prioritize applicants.

---
### How to Get Started
1.  *Open the Sidebar:* Click the > arrow in the top-left corner to see all available pages.
2.  *Navigate to the Checker:* Select *'Resume Checker'* from the sidebar to open the main tool.
3.  *Upload Documents:* Upload the candidate's PDF resume and the job description file (PDF or TXT).
4.  *Run the Analysis:* Click the *'Analyze Now'* button and wait a few moments for the AI to process the documents.
5.  *Review and Manage:* View the detailed analysis on the screen. You can then see all past results in the *'Dashboard & History'* or view top candidates in the *'Shortlisted Candidates'* page.
""")



# Add direct navigation button to Resume Checker
if st.button('Go to Resume Checker: PlacementIQ', key='goto_resume_checker'):
    st.switch_page('pages/resume.py')

# Remove any empty sidebar elements (no st.sidebar.empty() or similar)