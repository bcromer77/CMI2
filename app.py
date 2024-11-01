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

# Helper function to render tasks in a table format
def render_task_table(task_list):
    # Create a DataFrame for tasks
    df = pd.DataFrame(task_list)
    df["Status"] = df.apply(lambda row: "✔️ Completed" if row["Completed"] else "❌ Not Completed", axis=1)
    
    # Convert checkboxes into a list for rendering in a table
    checkboxes = [st.checkbox(task["Title"], value=task["Completed"], key=task["Key"]) for task in task_list]
    
    # Update the "Completed" status based on checkbox values
    for i, task in enumerate(task_list):
        task["Completed"] = checkboxes[i]

    # Display the DataFrame in a cleaner format
    st.table(df[["Title", "Description", "Status"]])

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Manage your content ideas and track their completion status.")

    # List of content ideas
    content_ideas = [
        {"Title": "Beginner’s Guide to Influencer Marketing", "Description": "A simple guide to understanding influencer marketing for tourism.", "Completed": False, "Key": "task_guide"},
        {"Title": "Checklist for Influencer Selection", "Description": "A detailed checklist to help choose the right influencers.", "Completed": False, "Key": "task_checklist"},
        {"Title": "Top 10 Red Flags to Avoid", "Description": "Highlights common mistakes when working with influencers.", "Completed": False, "Key": "task_red_flags"},
        {"Title": "Content Calendar Template", "Description": "A downloadable content calendar template for planning influencer campaigns.", "Completed": False, "Key": "task_calendar"},
        {"Title": "Mini Case Study Series", "Description": "Short success stories of effective influencer marketing campaigns.", "Completed": False, "Key": "task_case_studies"},
        {"Title": "Influencer Contract Basics", "Description": "A guide explaining the essentials of influencer contracts.", "Completed": False, "Key": "task_contract_basics"},
        {"Title": "Webinar: Influencer Marketing 101", "Description": "A free webinar covering the basics of influencer marketing.", "Completed": False, "Key": "task_webinar"},
        {"Title": "Social Media Compliance Infographic", "Description": "An easy-to-understand infographic on social media compliance rules.", "Completed": False, "Key": "task_infographic"}
    ]

    render_task_table(content_ideas)

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies and track their completion status.")

    # List of premium content
    premium_content = [
        {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Description": "In-depth training on crafting effective influencer strategies.", "Completed": False, "Key": "task_masterclass"},
        {"Title": "Influencer Vetting Toolkit", "Description": "Comprehensive tools for vetting and matching influencers.", "Completed": False, "Key": "task_vetting_toolkit"},
        {"Title": "Guide to Influencer Contracts", "Description": "Detailed guidance on creating and managing influencer contracts.", "Completed": False, "Key": "task_influencer_contracts"},
        {"Title": "Content Strategy Workshop", "Description": "Interactive workshop to build a strong content strategy.", "Completed": False, "Key": "task_content_strategy"},
        {"Title": "Full Case Study Library", "Description": "Access a library of full case studies for in-depth learning.", "Completed": False, "Key": "task_case_library"},
        {"Title": "Influencer Legal Toolkit", "Description": "All-in-one legal toolkit for influencer marketing compliance.", "Completed": False, "Key": "task_legal_toolkit"},
        {"Title": "Advanced Influencer Marketing Webinar Series", "Description": "Series of advanced webinars covering influencer marketing strategies.", "Completed": False, "Key": "task_advanced_webinar"}
    ]

    render_task_table(premium_content)

# Content Calendar Section
elif section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content efficiently.")

    # Generate a content calendar from today, spanning 30 days
    start_date = datetime.today()
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
    task_types = ["Freemium"] * 8 + ["Premium"] * 7

    calendar_df = pd.DataFrame({
        "Date": dates[:len(tasks)],
        "Task": tasks,
        "Type": task_types
    })
    st.dataframe(calendar_df, use_container_width=True)

# Other Sections (Viral Strategies, SEO Strategy, Notes & To-Do, Links & Resources, Course Tutors)
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral.")
    # (Viral strategies content)

elif section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")
    # (SEO strategy content)

elif section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")
    # (Notes & To-Do content)

elif section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")
    # (Links & Resources content)

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


