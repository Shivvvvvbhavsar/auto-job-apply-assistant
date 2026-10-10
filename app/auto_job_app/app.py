import streamlit as st

st.set_page_config(page_title="Auto Job Apply Assistant", page_icon="💼")

st.title("Auto Job Apply Assistant")
st.write("Your personal job search dashboard")

st.subheader("Job Preferences")

name = st.text_input("Your Name")
roles = st.text_input(
    "Target Job Roles",
    "Data Analyst, Business Analyst, MIS Analyst"
)
location = st.text_input("Preferred Location", "Pune")
skills = st.text_input("Your Skills", "Python, SQL, Excel, Power BI")

if st.button("Save Preferences"):
    st.session_state["profile"] = {
        "name": name,
        "roles": roles,
        "location": location,
        "skills": skills
    }
    st.success("Preferences saved!")

st.divider()
st.subheader("Job Application Tracker")
st.info("Next we will add job search and resume matching.")
