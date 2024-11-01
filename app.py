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

# Function to render tasks with checkboxes and update their status
def render_task_table(task_list):
    # Iterate through the tasks and create checkboxes
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

    # List of content ideas
    content_ideas = [
        {"Title": "Beginner’s Guide to Influencer Marketing", "Description": "A simple guide to understanding influencer marketing for tourism.", "Completed": False, "Key": "task_guide", "Status": "❌ Not Completed"},
        {"Title": "Checklist for Influencer Selection", "Description": "A detailed checklist to help choose the right influencers.", "Completed": False, "Key": "task_checklist", "Status": "❌ Not Completed"},
        {"Title": "Top 10 Red Flags to Avoid", "Description": "Highlights common mistakes when working with influencers.", "Completed": False, "Key": "task_red_flags", "Status": "❌ Not Completed"},
        {"Title": "Content Calendar Template", "Description": "A downloadable content calendar template for planning influencer campaigns.", "Completed": False, "Key": "task_calendar", "Status": "❌ Not Completed"},
        {"Title": "Mini Case Study Series", "Description": "Short success stories of effective influencer marketing campaigns.", "Completed": False, "Key": "task_case_studies", "Status": "❌ Not Completed"},
        {"Title": "Influencer Contract Basics", "Description": "A guide explaining the essentials of influencer contracts.", "Completed": False, "Key": "task_contract_basics", "Status": "❌ Not Completed"},
        {"Title": "Webinar: Influencer Marketing 101", "Description": "A free webinar covering the basics of influencer marketing.", "Completed": False, "Key": "task_webinar", "Status": "❌ Not Completed"},
        {"Title": "Social Media Compliance Infographic", "Description": "An easy-to-understand infographic on social media compliance rules.", "Completed": False, "Key": "task_infographic", "Status": "❌ Not Completed"}
    ]

    render_task_table(content_ideas)

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Manage your premium content strategies and track their completion status.")

    # List of premium content
    premium_content = [
        {"Title": "Masterclass: Influencer Strategy for Municipal Tourism", "Description": "In-depth training on crafting effective influencer strategies.", "Completed": False, "Key": "task_masterclass", "Status": "❌ Not Completed"},
        {"Title": "Influencer Vetting Toolkit", "Description": "Comprehensive tools for vetting and matching influencers.", "Completed": False, "Key": "task_vetting_toolkit", "Status": "❌ Not Completed"},
        {"Title": "Guide to Influencer Contracts", "Description": "Detailed guidance on creating and managing influencer contracts.", "Completed": False, "Key": "task_influencer_contracts", "Status": "❌ Not Completed"},
        {"Title": "Content Strategy Workshop", "Description": "Interactive workshop to build a strong content strategy.", "Completed": False, "Key": "task_content_strategy", "Status": "❌ Not Completed"},
        {"Title": "Full Case Study Library", "Description": "Access a library of full case studies for in-depth learning.", "Completed": False, "Key": "task_case_library", "Status": "❌ Not Completed"},
        {"Title": "Influencer Legal Toolkit", "Description": "All-in-one legal toolkit for influencer marketing compliance.", "Completed": False, "Key": "task_legal_toolkit", "Status": "❌ Not Completed"},
        {"Title": "Advanced Influencer Marketing Webinar Series", "Description": "Series of advanced webinars covering influencer marketing strategies.", "Completed": False, "Key": "task_advanced_webinar", "Status": "❌ Not Completed"}
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

# Section: Viral Strategies
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral and maximize reach.")

    st.subheader("1. Utilize Hashtags Effectively")
    st.write("""
    Research trending hashtags related to your industry or content theme. Use a mix of popular and niche hashtags to increase 
    your content's visibility and engagement. Tools like Hashtagify or All Hashtag can help identify the best hashtags.
    """)

    st.subheader("2. Collaborate with Micro-Influencers")
    st.write("""
    Partner with micro-influencers who have a highly engaged audience. Offering them exclusive freemium content to share 
    can create buzz and increase your brand's reach. Micro-influencers often have a more authentic connection with their 
    followers, making them powerful advocates.
    """)

    st.subheader("3. Run Contests or Giveaways")
    st.write("""
    Organize contests or giveaways where followers need to share your content or tag friends to participate. This not only 
    encourages engagement but also spreads your content organically. Make sure the prize is relevant and enticing to your 
    target audience.
    """)

    st.subheader("4. Create Interactive Content")
    st.write("""
    Use polls, quizzes, and Q&A sessions on platforms like Instagram Stories and LinkedIn. Interactive content encourages 
    participation and can boost visibility through social media algorithms. It also provides valuable insights into your 
    audience’s preferences.
    """)

    st.subheader("5. Leverage Email Marketing")
    st.write("""
    Send engaging email updates to your subscribers about your latest content. Include shareable content and a clear call 
    to action, encouraging your subscribers to spread the word. Personalize your emails to make the content more relatable 
    and impactful.
    """)

    st.write("These strategies, when used together, can amplify your content's reach and make it more likely to go viral. Experiment with different approaches and measure your results to see what works best for your brand.")

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


