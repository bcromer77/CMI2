import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Simulated data for content ideas
def load_data():
    data = pd.DataFrame({
        "Index": range(1, 11),
        "Title": [
            "10 Influencer Marketing Terms You Need to Know",
            "How to Identify the Right Influencer for Your Brand",
            "Step-by-Step: Launching Your First Influencer Campaign",
            "Why Every Marketer Should Care About Influencer Marketing",
            "Crafting the Perfect Influencer Brief",
            "The Ethics of Influencer Marketing",
            "5 Common Influencer Marketing Mistakes to Avoid",
            "Influencer Marketing on a Budget: Tips for Small Brands",
            "The Science of Influencer Audience Analysis",
            "How to Measure the ROI of Your Influencer Campaigns"
        ],
        "Subheadings": [
            "Glossary of Terms", "Defining Your Goals", "Planning",
            "The Rise of Influencers", "Key Elements of a Brief",
            "Importance of Authenticity", "Lessons Learned",
            "DIY Approaches", "Understanding Your Audience",
            "Defining ROI"
        ],
        "Notes_Angles": [
            "Definitions, Usage, Importance in Strategy",
            "Tools for Research, Metrics to Consider",
            "Checklists, Common Pitfalls, Case Studies",
            "Statistics, Market Analysis, Brand Examples",
            "Templates, Best Practices, Communication Tips",
            "FTC Guidelines, Transparency, Case Studies",
            "Lessons Learned, Consequences of Mistakes",
            "DIY Approaches, Budgeting Tips",
            "Demographics, Engagement Rates, Tools",
            "Examples, Calculation Methods, Importance of Accuracy"
        ],
        "Completed": [False] * 10
    })
    
    # Categorize content as Freemium or Premium
    freemium_titles = [
        "10 Influencer Marketing Terms You Need to Know",
        "How to Identify the Right Influencer for Your Brand",
        "Step-by-Step: Launching Your First Influencer Campaign",
        "Why Every Marketer Should Care About Influencer Marketing",
        "Crafting the Perfect Influencer Brief",
        "The Ethics of Influencer Marketing",
        "5 Common Influencer Marketing Mistakes to Avoid",
        "Influencer Marketing on a Budget: Tips for Small Brands"
    ]
    
    data["Category"] = data["Title"].apply(
        lambda x: "Freemium" if x in freemium_titles else "Premium"
    )
    return data

# Load the simulated data
if "content_data" not in st.session_state:
    st.session_state["content_data"] = load_data()

# Function to toggle task status
def toggle_task_status(index):
    st.session_state["content_data"].at[index, "Completed"] = not st.session_state["content_data"].at[index, "Completed"]

# Page Configuration
st.set_page_config(page_title="CMI Content Management Dashboard", layout="wide")

# Title and Introduction
st.title("CMI Content Management Dashboard")
st.subheader("Manage your content ideas efficiently and explore courses designed to master influencer marketing.")

# Sidebar Navigation
section = st.sidebar.radio("Go to:", [
    "Freemium Content",
    "Premium Content",
    "Content Calendar",
    "Course Tutors",
    "Courses"
])

# Freemium Content Section
if section == "Freemium Content":
    st.header("Freemium Content")
    st.write("Access high-value, free resources that introduce key concepts and best practices in influencer marketing.")
    st.markdown("---")

    # Filter and display freemium content
    freemium_content = st.session_state["content_data"][st.session_state["content_data"]["Category"] == "Freemium"]
    for index, row in freemium_content.iterrows():
        with st.expander(f"📋 {row['Title']}"):
            st.write(f"**Subheadings**: {row['Subheadings']}")
            st.write(f"**Notes/Angles**: {row['Notes_Angles']}")
            st.checkbox("Completed", value=row["Completed"], key=f"task_freemium_{index}", on_change=toggle_task_status, args=(index,))

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Gain exclusive access to in-depth training, masterclasses, and workshops to elevate your influencer marketing strategy.")
    st.markdown("---")

    # Filter and display premium content
    premium_content = st.session_state["content_data"][st.session_state["content_data"]["Category"] == "Premium"]
    for index, row in premium_content.iterrows():
        with st.expander(f"🌟 {row['Title']}"):
            st.write(f"**Subheadings**: {row['Subheadings']}")
            st.write(f"**Notes/Angles**: {row['Notes_Angles']}")
            st.checkbox("Completed", value=row["Completed"], key=f"task_premium_{index}", on_change=toggle_task_status, args=(index,))

# Content Calendar Section
elif section == "Content Calendar":
    st.header("Content Calendar for November")
    st.write("Plan and manage your content release schedule for the month of November.")
    st.markdown("---")

    # Generate a calendar for November
    start_date = datetime(2024, 11, 1)
    dates = [start_date + timedelta(days=i) for i in range(len(st.session_state["content_data"]))]
    calendar_df = pd.DataFrame({
        "Date": dates[:len(st.session_state["content_data"])],
        "Task": st.session_state["content_data"]["Title"],
        "Category": st.session_state["content_data"]["Category"],
        "Completed": st.session_state["content_data"]["Completed"]
    })
    st.dataframe(calendar_df, use_container_width=True)

# Course Tutors Section
elif section == "Course Tutors":
    st.header("Meet Our Expert Tutors")
    st.write("Learn from world-class experts who bring years of experience in marketing, storytelling, and public speaking.")
    st.markdown("---")

    # Example Tutor Profiles
    tutor_profiles = [
        {"Name": "Kay Munday", "Specialization": "Building Confidence", "Bio": "Leadership coach who empowers professionals to communicate confidently."},
        {"Name": "Dr. James McCabe", "Specialization": "Storytelling Narrative", "Bio": "Ph.D. in Communications, specializing in strategic storytelling."},
        {"Name": "Brian Jenner", "Specialization": "Rhetoric", "Bio": "Author and public speaking expert focused on the art of persuasion."}
    ]
    for tutor in tutor_profiles:
        with st.expander(f"👤 {tutor['Name']}"):
            st.write(f"**Specialization**: {tutor['Specialization']}")
            st.write(f"**Bio**: {tutor['Bio']}")

# Courses Section
elif section == "Courses":
    st.header("Explore Our Courses")
    st.write("Our courses are designed to take you from foundational concepts to advanced influencer marketing strategies.")
    st.markdown("---")

    # Example Course Offerings
    courses = [
        {"Title": "Reputation - RippleXp", "Description": "Top-of-funnel course for managing brand reputation through storytelling."},
        {"Title": "Influencer Marketing Masterclass", "Description": "Advanced strategies for building long-term relationships and measuring ROI."}
    ]
    for course in courses:
        with st.expander(f"📘 {course['Title']}"):
            st.write(course["Description"])

# Footer
st.write("---")
st.write("Ready to transform your marketing strategy? Start your RippleXp journey today.")
st.button("Contact Us for a Free Consultation")
