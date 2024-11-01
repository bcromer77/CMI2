import streamlit as st

# Page Configuration
st.set_page_config(page_title="CMI Content Management Dashboard", layout="wide")

# Title and Header
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
    "Course Tutors",
    "Courses"
])

# Section: Content Ideas
if section == "Content Ideas":
    st.header("Content Ideas")
    # Add your content ideas checklist and table code here
    st.write("Content Ideas checklist will go here.")

# Section: Premium Content
elif section == "Premium Content":
    st.header("Premium Content")
    # Add your premium content checklist and table code here
    st.write("Premium Content checklist will go here.")

# Section: Content Calendar
elif section == "Content Calendar":
    st.header("Content Calendar")
    # Add your content calendar code here
    st.write("Content Calendar details will go here.")

# Section: Viral Strategies
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral.")

# Section: SEO Strategy
elif section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")

# Section: Notes & To-Do
elif section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")

# Section: Links & Resources
elif section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")

# Section: Course Tutors
elif section == "Course Tutors":
    st.header("Course Tutors")
    st.write("Information about course tutors will go here.")

# Section: Courses
elif section == "Courses":
    st.header("Courses")
    # Add your course content here
    st.title("RippleXp - Transforming Brand Reputation Management")
    st.write("""
        ### Why Now?
        In a world where brands are constantly under the lens, the fear of reputational damage has never been more palpable. 
        **RippleXp** serves as a calling card, capitalizing on this urgency by empowering brands to understand and manage the 
        multiple narratives surrounding them online...
    """)
    # Continue with the content from your Reputation course

# Add more sections as needed



