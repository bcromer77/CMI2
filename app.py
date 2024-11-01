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
st.sidebar.markdown("- [Content Calendar Template](#content-calendar-template)", unsafe_allow_html=True)
st.sidebar.markdown("- [Mini Case Study Series](#mini-case-study-series)", unsafe_allow_html=True)
st.sidebar.markdown("- [Influencer Contract Basics](#influencer-contract-basics)", unsafe_allow_html=True)
st.sidebar.markdown("- [Webinar: Influencer Marketing 101](#webinar-influencer-marketing-101)", unsafe_allow_html=True)
st.sidebar.markdown("- [Social Media Compliance Infographic](#social-media-compliance-infographic)", unsafe_allow_html=True)

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")

    # Freemium Content with Neater Checkboxes
    st.subheader("Freemium Content")
    freemium_content = [
        {"Title": "Beginner’s Guide to Influencer Marketing", "Status": st.checkbox("Completed", key="freemium1")},
        {"Title": "Checklist for Influencer Selection", "Status": st.checkbox("Completed", key="freemium2")},
        {"Title": "Top 10 Red Flags to Avoid", "Status": st.checkbox("Completed", key="freemium3")},
        {"Title": "Content Calendar Template", "Status": st.checkbox("Completed", key="freemium4")},
        {"Title": "Mini Case Study Series", "Status": st.checkbox("Completed", key="freemium5")},
        {"Title": "Influencer Contract Basics", "Status": st.checkbox("Completed", key="freemium6")},
        {"Title": "Webinar: Influencer Marketing 101", "Status": st.checkbox("Completed", key="freemium7")},
        {"Title": "Social Media Compliance Infographic", "Status": st.checkbox("Completed", key="freemium8")}
    ]

    for item in freemium_content:
        st.write(f"{item['Title']} - {'✔️ Completed' if item['Status'] else '❌ Not Completed'}")

# Premium Content Section
if section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies here.")

    # Premium Content with Neater Checkboxes
    st.subheader("Premium Content")
    premium_content = [
        {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Status": st.checkbox("Completed", key="premium1")},
        {"Title": "Influencer Vetting Toolkit", "Status": st.checkbox("Completed", key="premium2")},
        {"Title": "Guide to Influencer Contracts", "Status": st.checkbox("Completed", key="premium3")},
        {"Title": "Content Strategy Workshop", "Status": st.checkbox("Completed", key="premium4")},
        {"Title": "Full Case Study Library", "Status": st.checkbox("Completed", key="premium5")},
        {"Title": "Influencer Legal Toolkit", "Status": st.checkbox("Completed", key="premium6")},
        {"Title": "Advanced Influencer Marketing Webinar Series", "Status": st.checkbox("Completed", key="premium7")},
        {"Title": "Compliance Masterclass", "Status": st.checkbox("Completed", key="premium8")}
    ]

    for content in premium_content:
        st.write(f"{content['Title']} - {'✔️ Completed' if content['Status'] else '❌ Not Completed'}")

# Content Calendar Section
if section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content with our content calendar.")

    # Generate a calendar starting from November 4th for 30 days
    start_date = datetime(2024, 11, 4)
    dates = [start_date + timedelta(days=i) for i in range(30)]
    calendar_tasks = [
        {"Task": "Beginner’s Guide to Influencer Marketing", "Type": "Freemium"},
        {"Task": "Checklist for Influencer Selection", "Type": "Freemium"},
        {"Task": "Top 10 Red Flags to Avoid", "Type": "Freemium"},
        {"Task": "Content Calendar Template", "Type": "Freemium"},
        {"Task": "Mini Case Study Series", "Type": "Freemium"},
        {"Task": "Influencer Contract Basics", "Type": "Freemium"},
        {"Task": "Webinar: Influencer Marketing 101", "Type": "Freemium"},
        {"Task": "Social Media Compliance Infographic", "Type": "Freemium"},
        {"Task": "Masterclass: Influencer Strategy for Municipal Tourism", "Type": "Premium"},
        {"Task": "Influencer Vetting Toolkit", "Type": "Premium"},
        {"Task": "Guide to Influencer Contracts", "Type": "Premium"},
        {"Task": "Content Strategy Workshop", "Type": "Premium"},
        {"Task": "Full Case Study Library", "Type": "Premium"},
        {"Task": "Influencer Legal Toolkit", "Type": "Premium"},
        {"Task": "Advanced Influencer Marketing Webinar Series", "Type": "Premium"},
        {"Task": "Compliance Masterclass", "Type": "Premium"}
    ]

    # Extend the tasks to fill 30 days if needed
    while len(calendar_tasks) < 30:
        calendar_tasks.append({"Task": "", "Type": ""})

    # Create DataFrame for the calendar
    calendar_df = pd.DataFrame({
        "Date": dates,
        "Task": [t["Task"] for t in calendar_tasks],
        "Type": [t["Type"] for t in calendar_tasks]
    })

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




