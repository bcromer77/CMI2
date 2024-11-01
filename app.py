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
    st.write("Here you can manage your content ideas.")

    # Creating the content table
    data = {
        "Content Type": ["Freemium", "Freemium", "Freemium", "Premium", "Premium"],
        "Title": [
            "Beginner’s Guide to Influencer Marketing",
            "Checklist for Influencer Selection",
            "Top 10 Red Flags to Avoid",
            "Masterclass: Influencer Strategy for Municipal Tourism",
            "Influencer Vetting Toolkit"
        ],
        "Description": [
            "A simple guide to understanding influencer marketing for tourism.",
            "A detailed checklist to help choose the right influencers.",
            "Highlights common mistakes when working with influencers.",
            "In-depth training on crafting effective influencer strategies.",
            "Comprehensive tools for vetting and matching influencers."
        ],
        "SEO Keywords": [
            "What is influencer marketing, Influencer marketing for tourism",
            "Influencer selection checklist, How to choose influencers",
            "Influencer red flags, Mistakes in influencer marketing",
            "Advanced influencer marketing, Tourism strategy masterclass",
            "Vetting influencers, Influencer matching system"
        ],
        "Call to Action": [
            "Download the guide",
            "Download the checklist",
            "Subscribe for more tips",
            "Enroll Now",
            "Purchase Toolkit"
        ],
        "Related Premium Content": [
            "Masterclass: Influencer Strategy for Municipal Tourism",
            "Influencer Vetting Toolkit",
            "Guide to Influencer Contracts",
            "Custom Consultation",
            "Advanced Analytics Suite"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

# Additional sections can be added for "Premium Content", "SEO Strategy", etc.
