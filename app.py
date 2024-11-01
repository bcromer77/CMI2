import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

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
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")

    # Example Freemium Content List
    freemium_content = [
        {"Title": "Beginner’s Guide to Influencer Marketing", "Status": False},
        {"Title": "Checklist for Influencer Selection", "Status": False},
        {"Title": "Top 10 Red Flags to Avoid", "Status": False},
        {"Title": "Content Calendar Template", "Status": False},
        {"Title": "Mini Case Study Series", "Status": False},
        {"Title": "Influencer Contract Basics", "Status": False},
        {"Title": "Webinar: Influencer Marketing 101", "Status": False},
        {"Title": "Social Media Compliance Infographic", "Status": False},
    ]

    # Display content list with checkboxes
    for item in freemium_content:
        item["Status"] = st.checkbox(item["Title"], value=item["Status"])
        st.write(f"Status: {'✔️ Completed' if item['Status'] else '❌ Not Completed'}")
        st.markdown("---")

if section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies here.")

    # Example Premium Content List
    premium_content = [
        {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Status": False},
        {"Title": "Influencer Vetting Toolkit", "Status": False},
        {"Title": "Guide to Influencer Contracts", "Status": False},
        {"Title": "Content Strategy Workshop", "Status": False},
        {"Title": "Full Case Study Library", "Status": False},
        {"Title": "Influencer Legal Toolkit", "Status": False},
        {"Title": "Advanced Influencer Marketing Webinar Series", "Status": False},
    ]

    # Display content list with checkboxes
    for item in premium_content:
        item["Status"] = st.checkbox(item["Title"], value=item["Status"])
        st.write(f"Status: {'✔️ Completed' if item['Status'] else '❌ Not Completed'}")
        st.markdown("---")

if section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content with our content calendar.")

    # Generate a calendar starting from November 4th for 30 days
    start_date = pd.Timestamp("2024-11-04")
    dates = [start_date + pd.Timedelta(days=i) for i in range(30)]
    calendar_tasks = [
        "Beginner’s Guide to Influencer Marketing",
        "Checklist for Influencer Selection",
        "Top 10 Red Flags to Avoid",
        "Content Calendar Template",
        "Mini Case Study Series",
        "Influencer Contract Basics",
        "Webinar: Influencer Marketing 101",
        "Social Media Compliance Infographic",
        "Masterclass: Influencer Strategy for Municipal Tourism",
        "Influencer Vetting Toolkit",
        "Guide to Influencer Contracts",
        "Content Strategy Workshop",
        "Full Case Study Library",
        "Influencer Legal Toolkit",
        "Advanced Influencer Marketing Webinar Series"
    ]
    types = ["Freemium"] * 8 + ["Premium"] * 7
    calendar_df = pd.DataFrame({"Date": dates[:len(calendar_tasks)], "Task": calendar_tasks, "Type": types})

    st.dataframe(calendar_df, use_container_width=True)
    st.write("Note: You can update the tasks manually in your personal copy.")

if section == "Viral Strategies":
    st.header("Strategies to Make Content Go Viral")
    st.write("1. **Utilize Hashtags**: Research trending hashtags for influencer marketing.")
    st.write("2. **Collaborate with Micro-Influencers**: Offer them your freemium content to share with their audience.")
    st.write("3. **Run Contests or Giveaways**: Encourage followers to share your content for a chance to win a premium resource.")
    st.write("4. **Create Interactive Content**: Use polls and quizzes on Instagram Stories and LinkedIn to engage your audience.")
    st.write("5. **Email Marketing**: Send updates to your subscribers about new content and encourage them to share with their network.")

if section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")

if section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")

if section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")

# New Course Tutors Section
if section == "Course Tutors":
    st.header("Course Tutors")
    st.write("Learn from our expert speakers:")
    st.write("**Building Confidence** - Kay Munday")
    st.write("**Storytelling Narrative** - Dr. James McCabe")
    st.write("**Rhetoric** - Brian Jenner")

# Aesthetic Enhancements
# Use custom colors and fonts
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
        color: #343a40;
        font-family: "Arial", sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #343a40;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)




