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

# Helper function for checkboxes and status updates
def render_task(title, description, completed_key):
    completed = st.checkbox(title, key=completed_key)
    status = "✔️ Completed" if completed else "❌ Not Completed"
    st.write(f"**Status:** {status}")
    st.write(description)
    st.markdown("---")

# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Manage your content ideas and track their completion status.")

    render_task("Beginner’s Guide to Influencer Marketing",
                "A simple guide to understanding influencer marketing for tourism.",
                "task_guide")

    render_task("Checklist for Influencer Selection",
                "A detailed checklist to help choose the right influencers.",
                "task_checklist")

    render_task("Top 10 Red Flags to Avoid",
                "Highlights common mistakes when working with influencers.",
                "task_red_flags")

    render_task("Content Calendar Template",
                "A downloadable content calendar template for planning influencer campaigns.",
                "task_calendar")

    render_task("Mini Case Study Series",
                "Short success stories of effective influencer marketing campaigns.",
                "task_case_studies")

    render_task("Influencer Contract Basics",
                "A guide explaining the essentials of influencer contracts.",
                "task_contract_basics")

    render_task("Webinar: Influencer Marketing 101",
                "A free webinar covering the basics of influencer marketing.",
                "task_webinar")

    render_task("Social Media Compliance Infographic",
                "An easy-to-understand infographic on social media compliance rules.",
                "task_infographic")

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies and track their completion status.")

    render_task("Masterclass: Influencer Strategy for Municipal Tourism",
                "In-depth training on crafting effective influencer strategies.",
                "task_masterclass")

    render_task("Influencer Vetting Toolkit",
                "Comprehensive tools for vetting and matching influencers.",
                "task_vetting_toolkit")

    render_task("Guide to Influencer Contracts",
                "Detailed guidance on creating and managing influencer contracts.",
                "task_influencer_contracts")

    render_task("Content Strategy Workshop",
                "Interactive workshop to build a strong content strategy.",
                "task_content_strategy")

    render_task("Full Case Study Library",
                "Access a library of full case studies for in-depth learning.",
                "task_case_library")

    render_task("Influencer Legal Toolkit",
                "All-in-one legal toolkit for influencer marketing compliance.",
                "task_legal_toolkit")

    render_task("Advanced Influencer Marketing Webinar Series",
                "Series of advanced webinars covering influencer marketing strategies.",
                "task_advanced_webinar")

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

# Viral Strategies Section
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral.")

    st.subheader("1. Utilize Trending Hashtags")
    st.write("Research and use trending hashtags relevant to your content. This increases visibility and connects your content to larger conversations happening online.")

    st.subheader("2. Collaborate with Micro-Influencers")
    st.write("Micro-influencers have highly engaged audiences. Collaborate with them to promote your freemium content. Their followers are more likely to engage with content that feels authentic.")

    st.subheader("3. Run Contests or Giveaways")
    st.write("Organize a contest or giveaway that encourages followers to share your content for a chance to win a premium resource. Make sure the rules are simple and engaging.")

    st.subheader("4. Create Interactive Content")
    st.write("Use polls, quizzes, and interactive stories on platforms like Instagram and LinkedIn. Engaging content is more likely to be shared, increasing reach and virality.")

    st.subheader("5. Leverage Email Marketing")
    st.write("Use email campaigns to announce new content. Include social sharing buttons and encourage subscribers to share the content with their network.")

    st.subheader("6. Optimize for Social Platforms")
    st.write("Tailor your content for each platform. Short videos work well on TikTok and Instagram, while in-depth articles may perform better on LinkedIn. Understand the unique characteristics of each platform to maximize impact.")

    st.subheader("7. Use Eye-Catching Visuals")
    st.write("High-quality images and videos are more likely to capture attention. Invest in good design to make your content stand out in crowded feeds.")

    st.subheader("8. Engage with Your Audience")
    st.write("Respond to comments, participate in conversations, and engage with your audience. The more interaction your content gets, the more likely it is to be amplified.")

# Other Sections (Placeholder)
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




