import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="CMI Content Management Dashboard", layout="wide")

# Home Page Title
st.title("CMI Content Management Dashboard")
st.subheader("Manage your content ideas efficiently.")

# Sidebar Navigation
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

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")

    # Content Ideas Data
    content_ideas = [
        {"Title": "Beginner’s Guide to Influencer Marketing", "Status": False},
        {"Title": "Checklist for Influencer Selection", "Status": False},
        {"Title": "Top 10 Red Flags to Avoid", "Status": False},
        {"Title": "Content Calendar Template", "Status": False},
        {"Title": "Mini Case Study Series", "Status": False},
        {"Title": "Influencer Contract Basics", "Status": False},
        {"Title": "Webinar: Influencer Marketing 101", "Status": False},
        {"Title": "Social Media Compliance Infographic", "Status": False},
    ]

    # Display Content Ideas with Toggle
    for item in content_ideas:
        item["Status"] = st.checkbox(f"{item['Title']} - {'✔️ Completed' if item['Status'] else '❌ Not Completed'}", value=item["Status"])

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies here.")

    # Premium Content Data
    premium_content = [
        {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Status": False},
        {"Title": "Influencer Vetting Toolkit", "Status": False},
        {"Title": "Guide to Influencer Contracts", "Status": False},
        {"Title": "Content Strategy Workshop", "Status": False},
        {"Title": "Full Case Study Library", "Status": False},
        {"Title": "Influencer Legal Toolkit", "Status": False},
        {"Title": "Advanced Influencer Marketing Webinar Series", "Status": False},
    ]

    # Display Premium Content with Toggle
    for item in premium_content:
        item["Status"] = st.checkbox(f"{item['Title']} - {'✔️ Completed' if item['Status'] else '❌ Not Completed'}", value=item["Status"])

# Content Calendar Section
elif section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content with our content calendar.")

    # Generate Calendar Data
    start_date = datetime(2024, 11, 4)
    dates = [start_date + timedelta(days=i) for i in range(30)]
    tasks = [
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

    # Create DataFrame for Calendar
    calendar_df = pd.DataFrame({"Date": dates[:len(tasks)], "Task": tasks, "Type": types})
    
    # Display Content Calendar
    st.dataframe(calendar_df, use_container_width=True)

# Additional Sections (Placeholder Text)
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral.")

elif section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")

elif section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")

elif section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")

elif section == "Course Tutors":
    st.header("Course Tutors")
    st.write("Learn from our expert speakers, each specializing in a unique aspect of brand reputation and storytelling:")
    st.subheader("Building Confidence")
    st.write("**Instructor:** Kay Munday")
    st.write("Kay Munday is an expert in helping professionals build confidence and presence in high-stakes situations. With years of experience in leadership coaching and public speaking, Kay has transformed countless professionals into confident, compelling communicators.")
    st.subheader("Storytelling Narrative")
    st.write("**Instructor:** Dr. James McCabe")
    st.write("Dr. James McCabe explores the art of storytelling as a strategic tool for brands. His sessions dive deep into crafting narratives that control and elevate brand reputation, making complex concepts accessible and actionable.")
    st.subheader("Rhetoric")
    st.write("**Instructor:** Brian Jenner")
    st.write("Brian Jenner specializes in the power of rhetoric, teaching professionals how to use persuasive language to influence and engage audiences effectively.")





