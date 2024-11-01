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

# Sample data from your provided lists (You can add all 120 items as needed)
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

premium_content = [
    {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Description": "In-depth training on crafting effective influencer strategies.", "Completed": False, "Key": "task_masterclass"},
    {"Title": "Influencer Vetting Toolkit", "Description": "Comprehensive tools for vetting and matching influencers.", "Completed": False, "Key": "task_vetting_toolkit"},
    {"Title": "Guide to Influencer Contracts", "Description": "Detailed guidance on creating and managing influencer contracts.", "Completed": False, "Key": "task_influencer_contracts"},
    {"Title": "Content Strategy Workshop", "Description": "Interactive workshop to build a strong content strategy.", "Completed": False, "Key": "task_content_strategy"},
    {"Title": "Full Case Study Library", "Description": "Access a library of full case studies for in-depth learning.", "Completed": False, "Key": "task_case_library"},
    {"Title": "Influencer Legal Toolkit", "Description": "All-in-one legal toolkit for influencer marketing compliance.", "Completed": False, "Key": "task_legal_toolkit"},
    {"Title": "Advanced Influencer Marketing Webinar Series", "Description": "Series of advanced webinars covering influencer marketing strategies.", "Completed": False, "Key": "task_advanced_webinar"}
]

# Function to render tasks with checkboxes and update their status
def render_task_table(task_list):
    for task in task_list:
        task["Completed"] = st.checkbox(task["Title"], value=task["Completed"], key=task["Key"])
        task["Status"] = "✔️ Completed" if task["Completed"] else "❌ Not Completed"
    
    # Convert task list to DataFrame and display as a table
    df = pd.DataFrame(task_list)
    st.table(df[["Title", "Description", "Status"]])

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Manage your content ideas and track their completion status.")
    render_task_table(content_ideas)

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies and track their completion status.")
    render_task_table(premium_content)

# Content Calendar Section
elif section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content efficiently.")

    # Generate a content calendar spanning 120 days
    start_date = datetime.today()
    dates = [start_date + timedelta(days=i) for i in range(120)]
    tasks = [idea["Title"] for idea in content_ideas] + [content["Title"] for content in premium_content]
    task_types = ["Freemium"] * len(content_ideas) + ["Premium"] * len(premium_content)

    calendar_df = pd.DataFrame({
        "Date": dates[:len(tasks)],
        "Task": tasks,
        "Type": task_types
    })
    st.dataframe(calendar_df, use_container_width=True)

# Section: Viral Strategies
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral and maximize reach.")
    st.subheader("1. Utilize Hashtags Effectively")
    st.write("Research trending hashtags related to your industry or content theme.")
    st.subheader("2. Collaborate with Micro-Influencers")
    st.write("Partner with micro-influencers who have a highly engaged audience.")
    st.subheader("3. Run Contests or Giveaways")
    st.write("Organize contests or giveaways to increase engagement.")
    st.subheader("4. Create Interactive Content")
    st.write("Use polls, quizzes, and Q&A sessions to boost interaction.")
    st.subheader("5. Leverage Email Marketing")
    st.write("Send engaging email updates to your subscribers.")

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
    st.write("Kay Munday is an expert in helping professionals build confidence.")
    st.subheader("Storytelling Narrative")
    st.write("**Instructor:** Dr. James McCabe")
    st.write("Dr. James McCabe explores the art of storytelling as a strategic tool.")
    st.subheader("Rhetoric")
    st.write("**Instructor:** Brian Jenner")
    st.write("Brian Jenner specializes in the power of rhetoric and persuasive language.")


