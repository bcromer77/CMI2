import streamlit as st

# Page Configuration
st.set_page_config(page_title="CMI Content Management Dashboard", layout="wide")

# Home Page Title
st.title("CMI Content Management Dashboard")
st.subheader("Manage your content ideas efficiently.")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", [
    "Home",
    "Content Ideas",
    "Premium Content",
    "Content Calendar",
    "Viral Strategies",
    "SEO Strategy",
    "Notes & To-Do",
    "Links & Resources",
    "Course Tutors"
])

# Course Tutors Section
if section == "Course Tutors":
    st.header("Course Tutors")
    st.write("Learn from our expert speakers, each specializing in a unique aspect of brand reputation and storytelling:")
    
    # Card for Kay Munday
    st.markdown("---")
    # st.image("path_to_kay_munday_image.jpg", width=150)  # Remove or replace with an actual image URL
    st.subheader("Building Confidence")
    st.write("**Instructor**: Kay Munday")
    st.write("""
    Kay Munday is an expert in helping professionals build confidence and presence in high-stakes situations. 
    With years of experience in leadership coaching and public speaking, Kay has transformed countless professionals 
    into confident, compelling communicators.
    """)
    st.button("Learn More", key="kay_button")
    
    # Card for Dr. James McCabe
    st.markdown("---")
    # st.image("path_to_james_mccabe_image.jpg", width=150)  # Remove or replace with an actual image URL
    st.subheader("Storytelling Narrative")
    st.write("**Instructor**: Dr. James McCabe")
    st.write("""
    Dr. James McCabe explores the art of storytelling as a strategic tool for brands. His sessions dive deep into 
    crafting narratives that control and elevate brand reputation, making complex concepts accessible and actionable.
    """)
    st.button("Learn More", key="james_button")
    
    # Card for Brian Jenner
    st.markdown("---")
    # st.image("path_to_brian_jenner_image.jpg", width=150)  # Remove or replace with an actual image URL
    st.subheader("Rhetoric")
    st.write("**Instructor**: Brian Jenner")
    st.write("""
    Brian Jenner specializes in the power of rhetoric, teaching techniques to persuade and influence in the corporate world. 
    With a background in speechwriting and corporate communications, Brian equips professionals with the rhetorical tools to 
    command attention and drive impact.
    """)
    st.button("Learn More", key="brian_button")

# Additional sections (e.g., Content Ideas, Premium Content, etc.) would follow...




