import streamlit as st
import json
from streamlit_js_eval import streamlit_js_eval
from Service import generate

# === New Tab ===
st.set_page_config(page_title="Colego - Cover Letter Generator", page_icon="🥑", layout="wide")

# === Page Style ===
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #fce4ec) !important;;
    background-size: cover;
    min-height: 100vh;
    color: #1a1a1a !important;
}

input[type="text"], textarea {
    border-radius: 8px !important;
    border: 0.05px solid #FFC0CB !important;
    padding: 10px !important;
    font-size: 15px !important;
}

div.stButton > button {
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    border: none;
    color: white;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.3s;
    width: 100%;
}

input, textarea, select, button {
    color: #1a1a1a !important;
    background-color: #ffffff !important;
}

label, .stTextInput label, .stTextArea label, .stSelectbox label {
    color: #1a1a1a !important;
    font-weight: 600 !important;
}

::placeholder {
    color: #666 !important;
    opacity: 1 !important;
}

.css-1d391kg, .stDataFrame, .stMarkdown table {
    color: #1a1a1a !important;
    background-color: #ffffff !important;
    border: 1px solid #ccc !important;
    border-radius: 8px !important;
}

div[data-testid="stNotification"], 
.stAlert, .stAlert > div {
    color: #1a1a1a !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# === Load if Saved ===
page_data = {
    "applicant_name": "",
    "applicant_email": "",
    "applicant_phone": "",
    "user_skills": "",
    "user_background": ""
}

local_data = streamlit_js_eval(js_expressions="localStorage.getItem('user_info')", key="get_user_info")

if local_data and isinstance(local_data, str):
    restored = json.loads(local_data)
    page_data.update(restored)

# === Title ===
st.markdown("<h1 style='text-align:center; margin-bottom:40px;'>🥑 Colego - AI Cover Letter Generator</h1>", unsafe_allow_html=True)

# ===~~~~~~~===
# === Forms ===
# ===~~~~~~~===
col1, col2, col3 = st.columns([3, 3, 4])

# === Personal Information ===
with col1:
    st.header("Personal Information")

    # == Info form ==
    with st.form(key='info_form'):
        applicant_name = st.text_input("Full Name", value=page_data.get("applicant_name", ""),
                                       placeholder="e.g. Colego")

        applicant_email = st.text_input("Email Address", value=page_data.get("applicant_email", ""),
                                        placeholder="e.g. email@example.com")

        applicant_phone = st.text_input("Phone Number", value=page_data.get("applicant_phone", ""),
                                        placeholder="e.g. 123-456-7890")

        user_skills = st.text_area("Technical & Soft Skills", value=page_data.get("user_skills", ""),
                                   placeholder="Please list your skills here.",
                                   height=150)

        user_background = st.text_area("Personal Background", value=page_data.get("user_background", ""),
                                       placeholder="Describe your academic background, experiences, career interests, etc...",
                                       height=500)

        st.markdown("<div style='font-size: 13px; color: gray; margin-top: -10px;'>"
                    "**This information helps generate a tailored cover letter."
                    "</div>", unsafe_allow_html=True)

        # == Save and Reset Button ==
        col1_1, col1_2 = st.columns([0.8, 1])
        with col1_1:
            save_button = st.form_submit_button("Save Information", help='Save your personal information to your local')
        with col1_2:
            reset_button = st.form_submit_button("Reset", help='Reset your personal information')

        # == Save Service ==
        if save_button:
            data = {
                "applicant_name": applicant_name,
                "applicant_email": applicant_email,
                "applicant_phone": applicant_phone,
                "user_skills": user_skills,
                "user_background": user_background
            }
            js_code = f"localStorage.setItem('user_info', JSON.stringify({json.dumps(data)}))"
            streamlit_js_eval(js_expressions=js_code, key="save_user_info")
            st.success("✅ Information saved successfully!")
        # == Reset Service ==
        if reset_button:
            streamlit_js_eval(js_expressions="localStorage.removeItem('user_info')", key="clear_user_info")
            st.success("🧹 Cleared saved data. Please refresh.")

# === Job Information ===
with col2:
    st.header("Job Information")

    # == Info form ==
    with st.form(key='Generator'):
        job_title = st.text_input("Position Title", placeholder="e.g. Software Engineer Intern")

        company_name = st.text_input("Company Name", placeholder="e.g. OpenAI")

        job_description = st.text_area(
            "Job Description",
            placeholder=(
                "Paste the full job description here.\n\n"
                "Include:\n"
                "- Required qualifications\n"
                "- Daily responsibilities\n"
                "- Technologies used\n"
                "- Desired soft skills"
            ),
            height=300
        )

        focus_points = st.text_area(
            "Cover Letter Focus (Optional)",
            placeholder=(
                "List traits or experiences to highlight.\n\n"
                "Examples:\n"
                "- Passion for AI research\n"
                "- Experience leading student clubs\n"
                "- Collaboration & problem-solving"
            ),
            height=200
        )

        st.markdown("<div style='font-size: 13px; color: gray; margin-top: -10px;'>"
                    "**Key Points or Strengths to Emphasize."
                    "</div>", unsafe_allow_html=True)

        # == Generate Button ==
        submit_button = st.form_submit_button(label='Generate Cover Letter')

# ===~~~~~~~~~~===
# === Generate ===
# ===~~~~~~~~~~===
with col3:
    st.header("Your Cover Letter")

    if submit_button:
        if not job_title or not company_name or not job_description:
            st.error("❗ Please fill in all required fields (title, company, and description)")
        else:
            with st.spinner("Generating your cover letter..."):

                # == Load Prompt ==
                with open("prompt.json", "r", encoding="utf-8") as f:
                    prompt = json.load(f)

                messages = []

                for i in prompt:
                    content = i["content"].format(
                        job_title=job_title,
                        company_name=company_name,
                        user_background=user_background,
                        user_skills=user_skills,
                        job_description=job_description,
                        applicant_name=applicant_name,
                        applicant_email=applicant_email,
                        applicant_phone=applicant_phone,
                        focus_points=focus_points
                    )
                    messages.append({"role": i["role"], "content": content})

                st.write(generate(messages))
    else:
        st.info("** Fill in the forms and click 'Generate Cover Letter' to your tailored cover letter here **")