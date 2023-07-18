from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Gajula Deepak.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Deepak Gajula | Digital CV"
PAGE_ICON = ":wave:"
NAME = "Deepak Gajula"
DESCRIPTION = """
Software Engineer, assisting aspiring programmer by teaching advanced python and technology's like data science and machine learning.
"""
EMAIL = "gdeepakdeepuml@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/deepudeepak1243/",
    "GitHub": "https://github.com/gdeepakdeepuml",
    "Kaggle": "https://www.kaggle.com/deepakdeepu8978l",
}
PROJECTS = {
    "🏆 13+ Machine learing use cases": "https://www.kaggle.com/deepakdeepu8978/code",
    "🏆 ML Doctor - Machine learning based web app for easy Diagnosis": "https://github.com/gdeepakdeepuml/ML-Doctor-",
    "🏆 Stock Forecasting App - This Stock Forecasting App can forecast 504 top companies stocks": "https://github.com/gdeepakdeepuml/Stock-Market-Forecasting-App",
    "🏆 COVIDBOT - complete end to end chat-bot with Pytorch for Covid-19 . this chat-bot can help to answer any question Corona": "https://github.com/gdeepakdeepuml/covidbot",

}
AWARDS = [
    "✨ AI/ML hackathon at KCG IT - Top 1 among 40+ teams",
    "✨ Infosys AI Hackathon - Top 5 among 50+ teams",
    "✨ Be the Change_Innovate - Earned badge for innovations done. " ,
    "✨ Kudos award - awarded for the innovations done.",
    "✨ DSC HITS core lead for Machine Learning - Facilitator for ML and DL" ,            
]


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in advanced Python 
- ✔️ Skilled in presenting complex Python topics in a clear and understandable manner.
- ✔️ experienced in making python automation frameworks and effective python techniques for creating web apps. 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming:	C/C++, advanced Python
- 💽 Version Control: Git,Github,VS-Code
- 📚 Machine Learning: Python with Tensorﬂow,Keras,PyTorch
- 📊 Data Visualisation: Matplotlib, Seaboarn, Scipy,Plotly
- 🌐 web applications: HTML5 and CSS, Streamlit

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**FIS Pvt Ltd, Bangalore, India  | software engineer**")
st.write("June 2022 - Precent")
st.write(
    """
- ► Working as a Devops engineer for the banking products speciﬁc to Fidelity National Information Services that supports reporting and analysis.
- ► Created a python-based applications for automation and interactive dashboard with real time data for internal usage.
- ► A Python framework was developed as part of automations to generate reports by verifying deployment parameters and to save time.
- ► A chatbot based on an LLM that enables users to converse with PDFs was developed as part of innovation.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Altimetrik India Pvt Ltd, chennai India | Machine Learning Eng Intern**")
st.write("Dec - Mar 2019")
st.write(
    """
- ► provided two functional real-time models. One of them is recognizing the hues of men's clothing.
- ► The second is deep learning-based pattern recognition algorithms for men's clothing.
- ► The very unbalanced collection of pixel values makes it difficult to discern colours. Utilising the k-means clustering approach for pixel clustering and OpenCV for colour identification, this problem was solved.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**MEIPORUL SOLUTIONS Pvt Ltd, Chennai India | Deep Learning Intern**")
st.write("March - May 2020")
st.write(
    """
- ► provided two real-time functioning models, one of which uses a chest x-ray and CT scan to estimate the covid-19.
- ► The second is a thorough investigation of Covid-19's global distribution and a patient monitoring dashboard.
- ► Complete analysis of COVID-19 by number of confirmed, recovered deaths, and active cases across the globe, with a focus on the top 5 countries: China (Wuhan), Italy, South Korea, Spain, and Iran, as well as Mortality & Recovery Rate and forecasting of confirmed, recovered deaths and cases using LSTM and exponential smoothing, ARIMA.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Awards & Recognitions ---
st.write('\n')
st.subheader("Awards & Recognitions")
st.write("---")
for award in AWARDS:
    st.write(f"{award}")