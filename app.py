import streamlit as st  # Ensure Streamlit is imported at the start
import pandas as pd
from datetime import datetime, timedelta

# Simulated data for content ideas with pricing
def load_data():
    data = pd.DataFrame({
        "Index": range(1, 16),
        "Title": [
            # Freemium Content
            "10 Influencer Marketing Terms You Need to Know",
            "How to Identify the Right Influencer for Your Brand",
            "Step-by-Step: Launching Your First Influencer Campaign",
            "Why Every Marketer Should Care About Influencer Marketing",
            "Crafting the Perfect Influencer Brief",
            "The Ethics of Influencer Marketing",
            "5 Common Influencer Marketing Mistakes to Avoid",
            "Influencer Marketing on a Budget: Tips for Small Brands",
            # Premium Content
            "The Science of Influencer Audience Analysis",
            "How to Measure the ROI of Your Influencer Campaigns",
            "Advanced Influencer Contract Negotiation",
            "Data-Driven Influencer Selection",
            "Crisis Management in Influencer Campaigns",
            "Legal Aspects of Influencer Marketing",
            "Building a Long-Term Influencer Program"
        ],
        "Subheadings": [
            # Freemium Content Subheadings
            "Glossary of Terms", "Defining Your Goals", "Planning",
            "The Rise of Influencers", "Key Elements of a Brief",
            "Importance of Authenticity", "Lessons Learned",
            "DIY Approaches",
            # Premium Content Subheadings
            "Understanding Your Audience", "Defining ROI",
            "Contract Essentials", "Analytics Tools Overview",
            "Crisis Response Strategies", "Legal Compliance 101",
            "Long-Term Strategy Planning"
        ],
        "Notes_Angles": [
            # Freemium Content Notes/Angles
            "Definitions, Usage, Importance in Strategy",
            "Tools for Research, Metrics to Consider",
            "Checklists, Common Pitfalls, Case Studies",
            "Statistics, Market Analysis, Brand Examples",
            "Templates, Best Practices, Communication Tips",
            "FTC Guidelines, Transparency, Case Studies",
            "Lessons Learned, Consequences of Mistakes",
            "DIY Approaches, Budgeting Tips",
            # Premium Content Notes/Angles
            "Demographics, Engagement Rates, Tools",
            "Examples, Calculation Methods, Importance of Accuracy",
            "Negotiation Tactics, Contract Templates",
            "Using Data for Strategic Selection",
            "Real-World Crisis Case Studies",
            "International Regulations, FTC Guidelines",
            "Sustaining Influencer Partnerships"
        ],
        "Delivery Format": [
            # Delivery Formats
            "Infographic (Canva Design)", "Interactive Checklist (PDF)", "Guide (PDF)",
            "Blog Post (Quick Read)", "Template (Downloadable PDF)",
            "Whitepaper (Downloadable)", "Quick Article", "Budget Guide (PDF)",
            "Masterclass (Video Series)", "Video Series",
            "E-book (PDF, $199)", "Interactive Webinar, $299",
            "Case Study Video Series, $249", "Online Course (Certification), $349",
            "Workshop (Workbook), $399"
        ],
        "Completed": [False] * 15
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

# Load the simulated data into session state
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
            st.write(f"**Best Delivery Format**: {row['Delivery Format']}")
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
            st.write(f"**Best Delivery Format & Pricing**: {row['Delivery Format']}")
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

    # Tutor Profiles
    tutor_profiles = [
        {
            "Name": "Kay Munday", 
            "Specialization": "Building Confidence", 
            "Bio": ("Kay Munday is an international speaker and coach dedicated to eradicating labels through storytelling. "
                    "She speaks on Women’s Empowerment, DEI, and Mental Health, drawing from her personal journey of overcoming "
                    "dyslexia and anxiety. As Google's go-to speaking coach, she transforms professionals into confident communicators.")
        },
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

    # Course Offerings
    courses = [
        {"Title": "Reputation - RippleXp", "Description": "Top-of-funnel course for managing
