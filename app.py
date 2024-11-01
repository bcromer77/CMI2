import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="RippleXp Content Management Dashboard", layout="wide")

# Home Page Title
st.title("RippleXp Content Management Dashboard")
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
    "Links & Resources"
])

# Sidebar Links for Freemium Content Ideas
st.sidebar.markdown("### What I Need to Build and Promote These Freemium Content Ideas")
st.sidebar.markdown("[Content Calendar Template](#content-calendar-template)", unsafe_allow_html=True)
st.sidebar.markdown("[Mini Case Study Series](#mini-case-study-series)", unsafe_allow_html=True)
st.sidebar.markdown("[Influencer Contract Basics](#influencer-contract-basics)", unsafe_allow_html=True)
st.sidebar.markdown("[Webinar: Influencer Marketing 101](#webinar-influencer-marketing-101)", unsafe_allow_html=True)
st.sidebar.markdown("[Social Media Compliance Infographic](#social-media-compliance-infographic)", unsafe_allow_html=True)

# Function to display content checklists
def display_content_checklist(content_data):
    for item in content_data:
        completed = st.checkbox(f"{item['Title']} - {'✔️ Completed' if item['Status'] == 'Completed' else '❌ Not Completed'}", value=item['Status'] == "Completed")
        if completed:
            item['Status'] = "Completed"
        else:
            item['Status'] = "Not Completed"

# Content Data for Freemium and Premium
freemium_content_data = [
    {"Title": "Beginner’s Guide to Influencer Marketing", "Status": "Not Completed"},
    {"Title": "Checklist for Influencer Selection", "Status": "Not Completed"},
    {"Title": "Top 10 Red Flags to Avoid", "Status": "Not Completed"},
    {"Title": "Content Calendar Template", "Status": "Not Completed"},
    {"Title": "Mini Case Study Series", "Status": "Not Completed"},
    {"Title": "Influencer Contract Basics", "Status": "Not Completed"},
    {"Title": "Webinar: Influencer Marketing 101", "Status": "Not Completed"},
    {"Title": "Social Media Compliance Infographic", "Status": "Not Completed"}
]

premium_content_data = [
    {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Status": "Not Completed"},
    {"Title": "Influencer Vetting Toolkit", "Status": "Not Completed"},
    {"Title": "Guide to Influencer Contracts", "Status": "Not Completed"},
    {"Title": "Content Strategy Workshop", "Status": "Not Completed"},
    {"Title": "Full Case Study Library", "Status": "Not Completed"},
    {"Title": "Influencer Legal Toolkit", "Status": "Not Completed"},
    {"Title": "Advanced Influencer Marketing Webinar Series", "Status": "Not Completed"}
]

# Main Content
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")
    display_content_checklist(freemium_content_data)

# Premium Content Section
if section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies here.")
    display_content_checklist(premium_content_data)

# Content Calendar Section
if section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content with our content calendar.")

    # Generate a calendar with both freemium and premium content
    start_date = pd.Timestamp("2024-11-04")
    dates = [start_date + pd.Timedelta(days=i) for i in range(len(freemium_content_data) + len(premium_content_data))]
    tasks = [item['Title'] for item in freemium_content_data + premium_content_data]
    types = ["Freemium"] * len(freemium_content_data) + ["Premium"] * len(premium_content_data)

    calendar_df = pd.DataFrame({
        "Date": dates,
        "Task": tasks,
        "Type": types
    })
    
    # Display the content calendar
    st.dataframe(calendar_df, use_container_width=True)
    st.write("Note: You can update the tasks manually in your personal copy.")

# Additional Sections
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




