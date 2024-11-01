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

    # Creating the content table with checkboxes
    content_data = [
        {
            "Content Type": "Freemium",
            "Title": "Beginner’s Guide to Influencer Marketing",
            "Description": "A simple guide to understanding influencer marketing for tourism.",
            "SEO Keywords": "What is influencer marketing, Influencer marketing for tourism",
            "Call to Action": "Download the guide",
            "Related Premium Content": "Masterclass: Influencer Strategy for Municipal Tourism",
            "Status": st.checkbox("Done", key="task1")
        },
        {
            "Content Type": "Freemium",
            "Title": "Checklist for Influencer Selection",
            "Description": "A detailed checklist to help choose the right influencers.",
            "SEO Keywords": "Influencer selection checklist, How to choose influencers",
            "Call to Action": "Download the checklist",
            "Related Premium Content": "Influencer Vetting Toolkit",
            "Status": st.checkbox("Done", key="task2")
        },
        {
            "Content Type": "Freemium",
            "Title": "Top 10 Red Flags to Avoid",
            "Description": "Highlights common mistakes when working with influencers.",
            "SEO Keywords": "Influencer red flags, Mistakes in influencer marketing",
            "Call to Action": "Subscribe for more tips",
            "Related Premium Content": "Guide to Influencer Contracts",
            "Status": st.checkbox("In Progress", key="task3")
        },
        {
            "Content Type": "Premium",
            "Title": "Masterclass: Influencer Strategy for Municipal Tourism",
            "Description": "In-depth training on crafting effective influencer strategies.",
            "SEO Keywords": "Advanced influencer marketing, Tourism strategy masterclass",
            "Call to Action": "Enroll Now",
            "Related Premium Content": "Custom Consultation",
            "Status": st.checkbox("Pending", key="task4")
        },
        {
            "Content Type": "Premium",
            "Title": "Influencer Vetting Toolkit",
            "Description": "Comprehensive tools for vetting and matching influencers.",
            "SEO Keywords": "Vetting influencers, Influencer matching system",
            "Call to Action": "Purchase Toolkit",
            "Related Premium Content": "Advanced Analytics Suite",
            "Status": st.checkbox("Pending", key="task5")
        }
    ]

    # Displaying the content table
    for item in content_data:
        st.markdown(f"**{item['Title']}**")
        st.write(item["Description"])
        st.write(f"**SEO Keywords:** {item['SEO Keywords']}")
        st.write(f"**Call to Action:** {item['Call to Action']}")
        st.write(f"**Related Premium Content:** {item['Related Premium Content']}")
        st.write(f"**Status:** {'✔️ Completed' if item['Status'] else '❌ Not Completed'}")
        st.markdown("---")


