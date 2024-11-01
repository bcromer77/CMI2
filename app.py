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

# Sidebar Links for Freemium Content Ideas
st.sidebar.markdown("### What I Need to Build and Promote These Freemium Content Ideas")
st.sidebar.markdown("[Content Calendar Template](#content-calendar-template)", unsafe_allow_html=True)
st.sidebar.markdown("[Mini Case Study Series](#mini-case-study-series)", unsafe_allow_html=True)
st.sidebar.markdown("[Influencer Contract Basics](#influencer-contract-basics)", unsafe_allow_html=True)
st.sidebar.markdown("[Webinar: Influencer Marketing 101](#webinar-influencer-marketing-101)", unsafe_allow_html=True)
st.sidebar.markdown("[Social Media Compliance Infographic](#social-media-compliance-infographic)", unsafe_allow_html=True)

# Main Content Sections
if section == "Course Tutors":
    st.header("Course Tutors")
    st.write("Learn from our expert speakers:")
    
    # Building Confidence - Kay Munday
    st.subheader("Building Confidence")
    st.write("**Instructor**: Kay Munday")
    st.write("Kay specializes in helping professionals build confidence and presence in high-stakes situations.")
    
    # Storytelling Narrative - Dr. James McCabe
    st.subheader("Storytelling Narrative")
    st.write("**Instructor**: Dr. James McCabe")
    st.write("""
        Dr. McCabe explores the art of storytelling as a strategic tool. Dive deep into the world of narratives and 
        discover how to craft stories that control and elevate your brand reputation.
        
        **RippleXp - Transforming Brand Reputation Management**
        
        ### Why Now?
        In a world where brands are constantly under the lens, the fear of reputational damage has never been more palpable. 
        **RippleXp** serves as a calling card, capitalizing on this urgency by empowering brands to understand and manage the 
        multiple narratives surrounding them online.
        
        Our approach is simple but powerful: use storytelling to uncover hidden risks and opportunities. Through dedicated 
        courses, RippleXp equips teams with insights and skills for proactive management, paving the way for RippleXn’s tools.
        
        **Key Sections of Dr. McCabe's Course**:
        - **Overview**: RippleXp as a top-of-funnel approach.
        - **Approach**: Storytelling for reputation management.
        - **Target Audiences**: Tailored solutions for varied audience stages.
        - **Entry-Level Products**: Easy entry into RippleXp’s ecosystem.
        - **Advanced Options**: Engaging sophisticated buyers with comprehensive courses.
        - **Crisis Identification Stages**: From detecting risks to proactive management.
        - **Course Assessment**: Customized recommendations for continued learning.
        
        **Ready to elevate your brand’s story?** Learn how RippleXp can transform your reputation strategy.
    """)
    
    # Rhetoric - Brian Jenner
    st.subheader("Rhetoric")
    st.write("**Instructor**: Brian Jenner")
    st.write("""
        Brian delves into the power of rhetoric, teaching techniques to persuade and influence effectively in the corporate world.
    """)

# Add remaining sections as necessary...



