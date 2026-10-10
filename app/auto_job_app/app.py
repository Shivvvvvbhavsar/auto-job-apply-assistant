import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Auto Job Apply Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# PROFESSIONAL CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #0B1120;
        color: #E5E7EB;
    }

    [data-testid="stHeader"] {
        background-color: rgba(11, 17, 32, 0.95);
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #263247;
    }

    [data-testid="stSidebar"] * {
        color: #E5E7EB;
    }

    .hero {
        background: linear-gradient(120deg, #172554 0%, #1E3A8A 55%, #2563EB 100%);
        padding: 32px;
        border-radius: 18px;
        margin-bottom: 28px;
        border: 1px solid #3556A5;
    }

    .hero h1 {
        color: #FFFFFF;
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        color: #DCE8FF;
        font-size: 15px;
        margin-bottom: 0;
    }

    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #F8FAFC;
        margin: 22px 0 8px 0;
    }

    .section-description {
        color: #94A3B8;
        font-size: 13px;
        margin-bottom: 22px;
    }

    .metric-card {
        background: #151F32;
        border: 1px solid #29374D;
        padding: 20px;
        border-radius: 14px;
        min-height: 112px;
    }

    .metric-label {
        color: #94A3B8;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 800;
        margin-top: 10px;
    }

    .panel {
        background: #111B2E;
        border: 1px solid #29374D;
        border-radius: 16px;
        padding: 24px;
        margin-top: 14px;
        margin-bottom: 20px;
    }

    .panel-heading {
        font-size: 18px;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 5px;
    }

    .panel-subtitle {
        color: #94A3B8;
        font-size: 13px;
        margin-bottom: 18px;
    }

    .stTextInput label,
    .stSelectbox label,
    .stMultiSelect label {
        color: #CBD5E1 !important;
        font-weight: 600 !important;
    }

    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div,
    .stMultiSelect div[data-baseweb="select"] > div {
        background-color: #172235 !important;
        color: #F8FAFC !important;
        border-color: #334155 !important;
        border-radius: 9px !important;
    }

    div[data-baseweb="select"] span {
        color: #F8FAFC !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #2563EB, #3B82F6);
        color: #FFFFFF;
        border: none;
        border-radius: 9px;
        font-weight: 700;
        padding: 11px 22px;
        min-height: 44px;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: #1D4ED8;
        color: #FFFFFF;
        border: none;
    }

    .stButton > button[kind="secondary"] {
        background: #1E293B;
        border: 1px solid #334155;
    }

    hr {
        border-color: #29374D;
    }

    .footer {
        text-align: center;
        color: #64748B;
        font-size: 12px;
        padding: 24px 0 10px 0;
    }

    [data-testid="stAlert"] {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# JOB ROLES
# --------------------------------------------------
JOB_ROLES = [
    # Software Development
    "Software Engineer",
    "Software Developer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Web Developer",
    "Mobile App Developer",
    "Android Developer",
    "iOS Developer",
    "React Developer",
    "Angular Developer",
    "Java Developer",
    "Python Developer",
    "C++ Developer",
    ".NET Developer",
    "PHP Developer",
    "WordPress Developer",
    "Embedded Software Engineer",
    "Game Developer",
    "QA Engineer",

    # AI and Machine Learning
    "AI Engineer",
    "Artificial Intelligence Engineer",
    "Machine Learning Engineer",
    "Deep Learning Engineer",
    "Generative AI Engineer",
    "Agentic AI Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",
    "Data Scientist",
    "Data Analyst",
    "Business Analyst",
    "Business Intelligence Analyst",
    "MIS Analyst",
    "BI Developer",
    "Data Engineer",
    "Analytics Engineer",
    "Big Data Engineer",
    "MLOps Engineer",
    "AI Research Engineer",
    "Research Scientist",
    "Prompt Engineer",
    "Robotics Engineer",
    "Research Analyst",

    # Cloud and DevOps
    "Cloud Engineer",
    "Cloud Architect",
    "AWS Cloud Engineer",
    "Azure Cloud Engineer",
    "Google Cloud Engineer",
    "DevOps Engineer",
    "Site Reliability Engineer",
    "Platform Engineer",
    "Infrastructure Engineer",
    "System Administrator",
    "Linux Administrator",
    "Network Engineer",
    "Database Administrator",
    "Database Developer",
    "SQL Developer",
    "Solutions Architect",
    "Technical Support Engineer",
    "IT Support Specialist",

    # Cybersecurity
    "Cybersecurity Analyst",
    "Security Analyst",
    "Information Security Analyst",
    "SOC Analyst",
    "Penetration Tester",
    "Ethical Hacker",
    "Security Engineer",
    "Cloud Security Engineer",
    "Application Security Engineer",
    "Security Consultant",
    "Digital Forensics Analyst",
    "GRC Analyst",
    "IAM Engineer",
    "Network Security Engineer",

    # Testing and Quality
    "Software Test Engineer",
    "Manual Tester",
    "Automation Test Engineer",
    "Selenium Tester",
    "Performance Test Engineer",
    "API Test Engineer",
    "SDET",
    "Quality Assurance Analyst",
    "Test Analyst",

    # Product and Project Management
    "Product Manager",
    "Associate Product Manager",
    "Technical Product Manager",
    "Project Manager",
    "IT Project Manager",
    "Program Manager",
    "Project Coordinator",
    "Scrum Master",
    "Agile Coach",
    "Product Owner",
    "Business Operations Analyst",
    "Product Analyst",
    "Technical Program Manager",

    # Design and User Experience
    "UI Designer",
    "UX Designer",
    "UI/UX Designer",
    "Product Designer",
    "Graphic Designer",
    "Web Designer",
    "Visual Designer",
    "Interaction Designer",
    "UX Researcher",
    "Motion Graphics Designer",
    "3D Designer",

    # Marketing and Media
    "Digital Marketing Executive",
    "Digital Marketing Analyst",
    "SEO Analyst",
    "SEO Specialist",
    "SEM Specialist",
    "Social Media Manager",
    "Social Media Executive",
    "Content Writer",
    "Technical Writer",
    "Copywriter",
    "Content Strategist",
    "Email Marketing Specialist",
    "Performance Marketing Analyst",
    "Marketing Analyst",
    "Brand Manager",
    "Marketing Manager",
    "Public Relations Executive",
    "Video Editor",
    "Multimedia Designer",

    # Finance and FinTech
    "Financial Analyst",
    "Finance Analyst",
    "Investment Analyst",
    "Equity Research Analyst",
    "Credit Analyst",
    "Risk Analyst",
    "Risk Management Analyst",
    "FinTech Analyst",
    "Financial Data Analyst",
    "Quantitative Analyst",
    "Accountant",
    "Auditor",
    "Tax Analyst",
    "Accounts Executive",
    "Treasury Analyst",
    "Banking Associate",
    "Business Finance Analyst",
    "Fraud Analyst",
    "Compliance Analyst",
    "Actuarial Analyst",

    # Consulting and Operations
    "Management Consultant",
    "Technology Consultant",
    "IT Consultant",
    "Strategy Analyst",
    "Operations Analyst",
    "Operations Executive",
    "Process Analyst",
    "Supply Chain Analyst",
    "Logistics Analyst",
    "Procurement Analyst",
    "Business Process Associate",
    "Management Trainee",
    "Research Associate",

    # Sales and Customer Success
    "Sales Executive",
    "Sales Analyst",
    "Business Development Executive",
    "Business Development Associate",
    "Business Development Manager",
    "Account Manager",
    "Key Account Manager",
    "Customer Success Associate",
    "Customer Success Manager",
    "Customer Support Executive",
    "Technical Account Manager",
    "Pre-Sales Engineer",
    "Salesforce Developer",
    "CRM Analyst",

    # HR and Administration
    "HR Executive",
    "HR Analyst",
    "HR Business Partner",
    "Talent Acquisition Specialist",
    "Recruiter",
    "Technical Recruiter",
    "Learning and Development Specialist",
    "Payroll Executive",
    "People Operations Analyst",
    "Administration Executive",

    # Hardware and Electronics
    "Electronics Engineer",
    "Hardware Engineer",
    "VLSI Design Engineer",
    "ASIC Design Engineer",
    "FPGA Engineer",
    "Firmware Engineer",
    "IoT Engineer",
    "Electrical Engineer",
    "Mechanical Engineer",
    "Automotive Software Engineer",

    # Entry-Level and Internship
    "Software Engineering Intern",
    "Data Analyst Intern",
    "Data Science Intern",
    "Machine Learning Intern",
    "AI Intern",
    "Python Developer Intern",
    "Web Development Intern",
    "Cybersecurity Intern",
    "Cloud Computing Intern",
    "Business Analyst Intern",
    "Research Intern",
    "Product Management Intern",
    "Digital Marketing Intern",
    "Finance Intern",
    "Graduate Engineer Trainee",
    "Software Trainee",
    "Technical Intern",
    "IT Intern",
    "Fresher",
]

JOB_ROLES = sorted(set(JOB_ROLES), key=str.casefold)

LOCATIONS = [
    "Any Location",
    "Pune",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Delhi NCR",
    "Noida",
    "Gurugram",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Indore",
    "Nagpur",
    "Nashik",
    "Chhatrapati Sambhajinagar",
    "Thane",
    "Kochi",
    "Coimbatore",
    "Lucknow",
    "Chandigarh",
    "Bhopal",
    "Remote - India",
    "Work From Home",
    "Outside India",
]

EXPERIENCE_LEVELS = [
    "Any Experience",
    "Internship",
    "Fresher",
    "Entry Level (0–2 years)",
    "Junior (1–3 years)",
    "Mid Level (3–5 years)",
    "Senior (5–8 years)",
    "Lead / Principal (8+ years)",
]


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "profile" not in st.session_state:
    st.session_state.profile = None


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 💼 JobPilot")
    st.caption("SMART JOB SEARCH PLATFORM")
    st.divider()

    st.markdown("### Navigation")
    st.markdown("🏠  Dashboard")
    st.markdown("👤  Job Preferences")
    st.markdown("📋  Application Tracker")
    st.markdown("🎯  Resume Matching")

    st.divider()

    st.markdown("### Account Status")
    if st.session_state.profile:
        st.success("Profile saved")
    else:
        st.info("Profile not configured")

    st.caption("Version 1.0.0")


# --------------------------------------------------
# HERO HEADER
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>Auto Job Apply Assistant</h1>
    <p>
        Your intelligent job search workspace.
        Manage your preferences, discover relevant opportunities,
        and organize your job applications in one place.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------
profile = st.session_state.profile

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Profile Status</div>
        <div class="metric-value">""" +
        ("Ready" if profile else "Setup") +
        """</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Target Roles</div>
        <div class="metric-value">""" +
        str(len(profile["roles"])) if profile else "0"
    , unsafe_allow_html=True)

    if profile:
        st.markdown("""
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Job Search</div>
        <div class="metric-value">""" +
        ("Configured" if profile else "Not Started") +
        """</div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# JOB PREFERENCES
# --------------------------------------------------
st.markdown('<div class="section-title">Job Preferences</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-description">'
    'Configure your profile to personalize your job search.'
    '</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    st.markdown("### 👤 Personal Information")
    st.caption("Tell us who you are and what opportunities you want.")

    name = st.text_input(
        "Full Name",
        value=profile["name"] if profile else "",
        placeholder="Enter your full name"
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_roles = st.multiselect(
            "Target Job Roles",
            options=JOB_ROLES,
            default=profile["roles"] if profile else [],
            placeholder="Search and select one or more roles",
            help="Type to search. You can select multiple job roles."
        )

    with col2:
        selected_location = st.selectbox(
            "Preferred Location",
            options=LOCATIONS,
            index=(
                LOCATIONS.index(profile["location"])
                if profile and profile["location"] in LOCATIONS
                else LOCATIONS.index("Pune")
            )
        )

    experience = st.selectbox(
        "Experience Level",
        options=EXPERIENCE_LEVELS,
        index=(
            EXPERIENCE_LEVELS.index(profile["experience"])
            if profile and profile["experience"] in EXPERIENCE_LEVELS
            else EXPERIENCE_LEVELS.index("Fresher")
        )
    )

    st.divider()

    save_col, reset_col = st.columns([2, 1])

    with save_col:
        save_clicked = st.button(
            "💾 Save Preferences",
            use_container_width=True,
            type="primary"
        )

    with reset_col:
        reset_clicked = st.button(
            "Reset Form",
            use_container_width=True
        )

    if save_clicked:
        if not name.strip():
            st.error("Please enter your full name.")
        elif not selected_roles:
            st.error("Please select at least one target job role.")
        else:
            st.session_state.profile = {
                "name": name.strip(),
                "roles": selected_roles,
                "location": selected_location,
                "experience": experience,
            }
            st.success("Your job preferences have been saved successfully!")
            st.rerun()

    if reset_clicked:
        st.session_state.profile = None
        st.rerun()


# --------------------------------------------------
# SAVED PROFILE SUMMARY
# --------------------------------------------------
if st.session_state.profile:
    profile = st.session_state.profile

    st.markdown(
        '<div class="section-title">Your Saved Profile</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown(f"### 👋 Welcome, {profile['name']}!")

        a, b = st.columns(2)

        with a:
            st.markdown("**Preferred Location**")
            st.write(f"📍 {profile['location']}")

            st.markdown("**Experience Level**")
            st.write(f"🎓 {profile['experience']}")

        with b:
            st.markdown("**Selected Job Roles**")
            for role in profile["roles"]:
                st.markdown(f"- {role}")


# --------------------------------------------------
# JOB APPLICATION TRACKER
# --------------------------------------------------
st.markdown(
    '<div class="section-title">Job Application Tracker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Your workspace for managing applications and tracking progress.'
    '</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    st.markdown("### 📋 Application Management")
    st.write(
        "Your application tracker will help you organize job openings, "
        "application dates, company details, interview stages, and outcomes."
    )

    st.info(
        "Coming next: Job search integration, resume matching, "
        "application tracking, and job recommendations."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer">
    JobPilot · Auto Job Apply Assistant · Built with Streamlit
    <br>
    Find opportunities. Organize applications. Move your career forward.
</div>
""", unsafe_allow_html=True)
