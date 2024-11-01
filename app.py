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

# Content for Viral Strategies Section
if section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral.")

    # List of Viral Strategies
    st.subheader("1. Utilize Trending Hashtags")
    st.write("""
    Research and use trending hashtags relevant to your content. This increases visibility and connects your content to larger conversations happening online.
    """)

    st.subheader("2. Collaborate with Micro-Influencers")
    st.write("""
    Micro-influencers have highly engaged audiences. Collaborate with them to promote your freemium content. Their followers are more likely to engage with content that feels authentic.
    """)

    st.subheader("3. Run Contests or Giveaways")
    st.write("""
    Organize a contest or giveaway that encourages followers to share your content for a chance to win a premium resource. Make sure the rules are simple and engaging.
    """)

    st.subheader("4. Create Interactive Content")
    st.write("""
    Use polls, quizzes, and interactive stories on platforms like Instagram and LinkedIn. Engaging content is more likely to be shared, increasing reach and virality.
    """)

    st.subheader("5. Leverage Email Marketing")
    st.write("""
    Use email campaigns to announce new content. Include social sharing buttons and encourage subscribers to share the content with their network.
    """)

    st.subheader("6. Optimize for Social Platforms")
    st.write("""
    Tailor your content for each platform. Short videos work well on TikTok and Instagram, while in-depth articles may perform better on LinkedIn. Understand the unique characteristics of each platform to maximize impact.
    """)

    st.subheader("7. Use Eye-Catching Visuals")
    st.write("""
    High-quality images and videos are more likely to capture attention. Invest in good design to make your content stand out in crowded feeds.
    """)

    st.subheader("8. Engage with Your Audience")
    st.write("""
    Respond to comments, participate in conversations, and engage with your audience. The more interaction your content gets, the more likely it is to be amplified.
    """)

# Other Sections (Placeholder)
elif section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas with task statuses.")
    # (Content Ideas logic goes here)

elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies here.")
    # (Premium Content logic goes here)

elif section == "Content Calendar":
    st.header("Content Calendar")
    st.write("Plan and manage your content with our content calendar.")
    # (Content Calendar logic goes here)

elif section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")
    # (SEO Strategy logic goes here)

elif section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")
    # (Notes & To-Do logic goes here)

elif section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")
    # (Links & Resources logic goes here)

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




