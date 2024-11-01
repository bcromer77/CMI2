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

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")

    # Creating the content table with toggles
    content_data = [
        {"Title": "Beginner’s Guide to Influencer Marketing", "Status": "❌ Not Completed"},
        {"Title": "Checklist for Influencer Selection", "Status": "❌ Not Completed"},
        {"Title": "Top 10 Red Flags to Avoid", "Status": "❌ Not Completed"},
        {"Title": "Content Calendar Template", "Status": "❌ Not Completed"},
        {"Title": "Mini Case Study Series", "Status": "❌ Not Completed"},
        {"Title": "Influencer Contract Basics", "Status": "❌ Not Completed"},
        {"Title": "Webinar: Influencer Marketing 101", "Status": "❌ Not Completed"},
        {"Title": "Social Media Compliance Infographic", "Status": "❌ Not Completed"}
    ]

    # Display content ideas
    for item in content_data:
        st.write(f"{item['Title']} - {item['Status']}")

# Premium Content Section
if section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies here.")
    
    premium_content_data = [
        {
            "Title": "Masterclass: Influencer Strategy for Municipal Tourism",
            "Description": "In-depth training on crafting effective influencer strategies.",
            "Call to Action": "Enroll Now",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Influencer Vetting Toolkit",
            "Description": "Comprehensive tools for vetting and matching influencers.",
            "Call to Action": "Purchase Toolkit",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Guide to Influencer Contracts",
            "Description": "Detailed guide to structuring influencer contracts to protect your brand.",
            "Call to Action": "Download the Guide",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Content Strategy Workshop",
            "Description": "Interactive workshop to improve your content strategy for influencer campaigns.",
            "Call to Action": "Sign Up for the Workshop",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Full Case Study Library",
            "Description": "Access to a full library of successful influencer marketing case studies.",
            "Call to Action": "Access Library",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Influencer Legal Toolkit",
            "Description": "Toolkit with all the legal resources needed for influencer campaigns.",
            "Call to Action": "Get the Toolkit",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Advanced Influencer Marketing Webinar Series",
            "Description": "Webinar series covering advanced topics in influencer marketing.",
            "Call to Action": "Register for the Series",
            "Status": "❌ Not Completed"
        },
        {
            "Title": "Compliance Masterclass",
            "Description": "Masterclass on navigating compliance in influencer marketing.",
            "Call to Action": "Join the Masterclass",
            "Status": "❌ Not Completed"
        }
    ]

    # Display premium content
    for content in premium_content_data:
        st.markdown(f"**{content['Title']}**")
        st.write(content["Description"])
        st.write(f"**Call to Action:** {content['Call to Action']}")
        st.write(f"**Status:** {content['Status']}")
        st.markdown("---")

# Content Calendar Section
if section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content with our content calendar.")

    # Generate a calendar starting from November 4th for 30 days
    start_date = datetime(2024, 11, 4)
    dates = [start_date + timedelta(days=i) for i in range(30)]
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
        "Advanced Influencer Marketing Webinar Series",
        "Compliance Masterclass"
    ]

    # Extend the calendar tasks to 30 days
    calendar_tasks.extend([""] * (30 - len(calendar_tasks)))

    # Create DataFrame for calendar
    calendar_df = pd.DataFrame({"Date": dates, "Task": calendar_tasks})
    
    # Display the calendar
    st.dataframe(calendar_df, use_container_width=True)
    st.write("Note: You can update tasks as needed.")

# Viral Strategies Section
if section == "Viral Strategies":
    st.header("Strategies to Make Content Go Viral")
    st.write("1. **Utilize Hashtags**: Research trending hashtags for influencer marketing.")
    st.write("2. **Collaborate with Micro-Influencers**: Offer them your freemium content to share with their audience.")
    st.write("3. **Run Contests or Giveaways**: Encourage followers to share your content for a chance to win a premium resource.")
    st.write("4. **Create Interactive Content**: Use polls and quizzes on Instagram Stories and LinkedIn to engage your audience.")
    st.write("5. **Email Marketing**: Send updates to your subscribers about new content and encourage them to share with their network.")

# Additional Sections
if section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")

if section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")

if section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")



