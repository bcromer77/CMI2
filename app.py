import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="RippleXp Content Management Dashboard", layout="wide")

# Home Page Title
st.title("RippleXp Content Management Dashboard")
st.subheader("Manage your content ideas efficiently.")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Content Ideas", "Premium Content", "SEO Strategy", "Notes & To-Do", "Links & Resources"])

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")

    # Creating the content table with toggles
    content_data = [
        {
            "Content Type": "Freemium",
            "Title": "Beginner’s Guide to Influencer Marketing",
            "Description": "A simple guide to understanding influencer marketing for tourism.",
            "SEO Keywords": "What is influencer marketing, Influencer marketing for tourism",
            "Call to Action": "Download the guide",
            "Related Premium Content": "Masterclass: Influencer Strategy for Municipal Tourism",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task1")
        },
        {
            "Content Type": "Freemium",
            "Title": "Checklist for Influencer Selection",
            "Description": "A detailed checklist to help choose the right influencers.",
            "SEO Keywords": "Influencer selection checklist, How to choose influencers",
            "Call to Action": "Download the checklist",
            "Related Premium Content": "Influencer Vetting Toolkit",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task2")
        },
        {
            "Content Type": "Freemium",
            "Title": "Top 10 Red Flags to Avoid",
            "Description": "Highlights common mistakes when working with influencers.",
            "SEO Keywords": "Influencer red flags, Mistakes in influencer marketing",
            "Call to Action": "Subscribe for more tips",
            "Related Premium Content": "Guide to Influencer Contracts",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task3")
        },
        {
            "Content Type": "Freemium",
            "Title": "Content Calendar Template",
            "Description": "A downloadable content calendar template for planning influencer campaigns.",
            "SEO Keywords": "Content calendar template, Influencer marketing planner",
            "Call to Action": "Download the template",
            "Related Premium Content": "Content Strategy Workshop",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task6")
        },
        {
            "Content Type": "Freemium",
            "Title": "Mini Case Study Series",
            "Description": "Short success stories of effective influencer marketing campaigns.",
            "SEO Keywords": "Influencer case studies, Marketing success stories",
            "Call to Action": "Read the case studies",
            "Related Premium Content": "Full Case Study Library",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task7")
        },
        {
            "Content Type": "Freemium",
            "Title": "Influencer Contract Basics",
            "Description": "A guide explaining the essentials of influencer contracts.",
            "SEO Keywords": "Influencer contract basics, Legal guide for influencer marketing",
            "Call to Action": "Download the guide",
            "Related Premium Content": "Influencer Legal Toolkit",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task8")
        },
        {
            "Content Type": "Freemium",
            "Title": "Webinar: Influencer Marketing 101",
            "Description": "A free webinar covering the basics of influencer marketing.",
            "SEO Keywords": "Influencer marketing webinar, Beginner's guide to influencer marketing",
            "Call to Action": "Register for the webinar",
            "Related Premium Content": "Advanced Influencer Marketing Webinar Series",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task9")
        },
        {
            "Content Type": "Freemium",
            "Title": "Social Media Compliance Infographic",
            "Description": "An easy-to-understand infographic on social media compliance rules.",
            "SEO Keywords": "Social media compliance, Influencer marketing infographic",
            "Call to Action": "Share the infographic",
            "Related Premium Content": "Compliance Masterclass",
            "Status": st.selectbox("Status", ["Not Completed", "Completed"], key="task10")
        }
    ]

    # Displaying the content table
    for item in content_data:
        st.markdown(f"**{item['Title']}**")
        st.write(item["Description"])
        st.write(f"**SEO Keywords:** {item['SEO Keywords']}")
        st.write(f"**Call to Action:** {item['Call to Action']}")
        st.write(f"**Related Premium Content:** {item['Related Premium Content']}")
        st.write(f"**Status:** {'✔️ Completed' if item['Status'] == 'Completed' else '❌ Not Completed'}")
        st.markdown("---")



