import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Simulated data for content ideas with pricing
def load_data():
    data = pd.DataFrame({
        "Index": range(1, 16),
        "Title": [
            # Freemium Content
            "10 Influencer Marketing Terms You Need to Know",
            "How to Identify the Right Influencer for Your Brand",
            "Step-by-Step: Launching Your First Influencer Campaign",
            "Why Every Marketer Should Care About Influencer Marketing",
            "Crafting the Perfect Influencer Brief",
            "The Ethics of Influencer Marketing",
            "5 Common Influencer Marketing Mistakes to Avoid",
            "Influencer Marketing on a Budget: Tips for Small Brands",
            # Premium Content
            "The Science of Influencer Audience Analysis",
            "How to Measure the ROI of Your Influencer Campaigns",
            "Advanced Influencer Contract Negotiation",
            "Data-Driven Influencer Selection",
            "Crisis Management in Influencer Campaigns",
            "Legal Aspects of Influencer Marketing",
            "Building a Long-Term Influencer Program"
        ],
        "Subheadings": [
            "Glossary of Terms", "Defining Your Goals", "Planning",
            "The Rise of Influencers", "Key Elements of a Brief",
            "Importance of Authenticity", "Lessons Learned",
            "DIY Approaches",
            "Understanding Your Audience", "Defining ROI",
            "Contract Essentials", "Analytics Tools Overview",
            "Crisis Response Strategies", "Legal Compliance 101",
            "Long-Term Strategy Planning"
        ],
        "Notes_Angles": [
            "Definitions, Usage, Importance in Strategy",
            "Tools for Research, Metrics to Consider",
            "Checklists, Common Pitfalls, Case Studies",
            "Statistics, Market Analysis, Brand Examples",
            "Templates, Best Practices, Communication Tips",
            "FTC Guidelines, Transparency, Case Studies",
            "Lessons Learned, Consequences of Mistakes",
            "DIY Approaches, Budgeting Tips",
            "Demographics, Engagement Rates, Tools",
            "Examples, Calculation Methods, Importance of Accuracy",
            "Negotiation Tactics, Contract Templates",
            "Using Data for Strategic Selection",
            "Real-World Crisis Case Studies",
            "International Regulations, FTC Guidelines",
            "Sustaining Influencer Partnerships"
        ],
        "Delivery Format": [  # Double-check the exact name here
            "Infographic (Canva Design)", "Interactive Checklist (PDF)", "Guide (PDF)",
            "Blog Post (Quick Read)", "Template (Downloadable PDF)",
            "Whitepaper (Downloadable)", "Quick Article", "Budget Guide (PDF)",
            "Masterclass (Video Series)", "Video Series",
            "E-book (PDF, $199)", "Interactive Webinar, $299",
            "Case Study Video Series, $249", "Online Course (Certification), $349",
            "Workshop (Workbook), $399"
        ],
        "Completed": [False] * 15
    })

    # Print column names to check
    print(data.columns)

    # Categorize content as Freemium or Premium
    freemium_titles = [
        "10 Influencer Marketing Terms You Need to Know",
        "How to Identify the Right Influencer for Your Brand",
        "Step-by-Step: Launching Your First Influencer Campaign",
        "Why Every Marketer Should Care About Influencer Marketing",
        "Crafting the Perfect Influencer Brief",
        "The Ethics of Influencer Marketing",
        "5 Common Influencer Marketing Mistakes to Avoid",
        "Influencer Marketing on a Budget: Tips for Small Brands"
    ]
    
    data["Category"] = data["Title"].apply(
        lambda x: "Freemium" if x in freemium_titles else "Premium"
    )
    return data

# Load the simulated data into session state
if "content_data" not in st.session_state:
    st.session_state["content_data"] = load_data()

# Function to toggle task status
def toggle_task_status(index):
    st.session_state["content_data"].at[index, "Completed"] = not st.session_state["content_data"].at[index, "Completed"]

# Page Configuration
st.set_page_config(page_title="CMI Content Management Dashboard", layout="wide")

# Title and Introduction
st.title("CMI Content Management Dashboard")
st.subheader("Manage your content ideas efficiently and explore courses designed to master influencer marketing.")

# Sidebar Navigation
section = st.sidebar.radio("Go to:", [
    "Freemium Content",
    "Premium Content",
    "Content Calendar",
    "Course Tutors",
    "Courses"
])

# Freemium Content Section
if section == "Freemium Content":
    st.header("Freemium Content")
    st.write("Access high-value, free resources that introduce key concepts and best practices in influencer marketing.")
    st.markdown("---")

    # Filter and display freemium content
    freemium_content = st.session_state["content_data"][st.session_state["content_data"]["Category"] == "Freemium"]
    for index, row in freemium_content.iterrows():
        with st.expander(f"📋 {row['Title']}"):
            st.write(f"**Subheadings**: {row['Subheadings']}")
            st.write(f"**Notes/Angles**: {row['Notes_Angles']}")
            st.write(f"**Best Delivery Format**: {row['Delivery Format']}")
            st.checkbox("Completed", value=row["Completed"], key=f"task_freemium_{index}", on_change=toggle_task_status, args=(index,))

# Premium Content Section
elif section == "Premium Content":
    st.header("Premium Content")
    st.write("Gain exclusive access to in-depth training, masterclasses, and workshops to elevate your influencer marketing strategy.")
    st.markdown("---")

    # Filter and display premium content
    premium_content = st.session_state["content_data"][st.session_state["content_data"]["Category"] == "Premium"]
    for index, row in premium_content.iterrows():
        with st.expander(f"🌟 {row['Title']}"):
            st.write(f"**Subheadings**: {row['Subheadings']}")
            st.write(f"**Notes/Angles**: {row['Notes_Angles']}")
            st.write(f"**Best Delivery Format & Pricing**: {row['Delivery Format']}")
            st.checkbox("Completed", value=row["Completed"], key=f"task_premium_{index}", on_change=toggle_task_status, args=(index,))

# Content Calendar Section
elif section == "Content Calendar":
    st.header("Content Calendar for November")
    st.write("Plan and manage your content release schedule for the month of November.")
    st.markdown("---")

    # Generate a calendar for November
    start_date = datetime(2024, 11, 1)
    dates = [start_date + timedelta(days=i) for i in range(len(st.session_state["content_data"]))]
    calendar_df = pd.DataFrame({
        "Date": dates[:len(st.session_state["content_data"])],
        "Task": st.session_state["content_data"]["Title"],
        "Category": st.session_state["content_data"]["Category"],
        "Completed": st.session_state["content_data"]["Completed"]
    })
    st.dataframe(calendar_df, use_container_width=True)

# Course Tutors Section
elif section == "Course Tutors":
    st.header("Meet Our Expert Tutors")
    st.write("Learn from world-class experts who bring years of experience in marketing, storytelling, and public speaking.")
    st.markdown("---")

    # Tutor Profiles
    tutor_profiles = [
        {
            "Name": "Kay Munday", 
            "Specialization": "Building Confidence", 
            "Bio": ("Kay Munday is an international speaker and coach dedicated to eradicating labels through storytelling. "
                    "She speaks on Women’s Empowerment, DEI, and Mental Health, drawing from her personal journey of overcoming "
                    "dyslexia and anxiety. As Google's go-to speaking coach, she transforms professionals into confident communicators.")
        },
        {"Name": "Dr. James McCabe", "Specialization": "Storytelling Narrative", "Bio": "Ph.D. in Communications, specializing in strategic storytelling."},
        {"Name": "Brian Jenner", "Specialization": "Rhetoric", "Bio": "Author and public speaking expert focused on the art of persuasion."}
    ]
    for tutor in tutor_profiles:
        with st.expander(f"👤 {tutor['Name']}"):
            st.write(f"**Specialization**: {tutor['Specialization']}")
            st.write(f"**Bio**: {tutor['Bio']}")
# RippleXp Courses Section
if section == "Courses":
    # Add RippleXp Content Here
    st.title("RippleXp - Transforming Brand Reputation Management")
    st.write("""
        ### Why Now?
        In a world where brands are constantly under the lens, the fear of reputational damage has never been more palpable. 
        **RippleXp** serves as a calling card, capitalizing on this urgency by empowering brands to understand and manage the 
        multiple narratives surrounding them online. By leveraging the fear of reputational damage, RippleXp offers a gateway 
        to RippleXn’s deeper social listening and reputation management services.
        
        Our approach is simple but powerful: use storytelling to uncover hidden risks and opportunities, allowing brands to 
        engage in self-reflection and proactive management. Through dedicated, hands-on courses, RippleXp equips teams with 
        the insights and skills they need to navigate today’s high-stakes media landscape. **The Trojan horse?** RippleXp 
        positions brands to embrace RippleXn’s full suite of social listening tools for ongoing protection.
    """)
    st.write("---")

    # RippleXp Course Navigation
    ripple_section = st.radio("Course Navigation", [
        "Overview", 
        "The RippleXp Approach", 
        "Target Audiences", 
        "Entry-Level Products", 
        "Advanced Options", 
        "Commercialization & Off-the-Shelf Products", 
        "Crisis Identification Stages", 
        "Course Assessment"
    ])

    # Content for Each RippleXp Subsection
    if ripple_section == "Overview":
        st.header("Overview: RippleXp as a Top-of-Funnel Approach")
        st.write("RippleXp acts as a strategic top-of-funnel entry point for RippleXn’s core offerings...")

    elif ripple_section == "The RippleXp Approach":
        st.header("The RippleXp Approach to Reputation Management")
        st.write("Reputation is a mosaic, composed of hundreds of individual stories...")

    elif ripple_section == "Target Audiences":
        st.header("Target Audiences - Four Key Areas of Focus")
        st.write("RippleXp courses are tailored to address the different stages of brand audience engagement...")

    elif ripple_section == "Entry-Level Products":
        st.header("Entry-Level Products for Customer Acquisition")
        st.write("These offerings serve as introductory tools to bring clients into the RippleXp ecosystem...")

    elif ripple_section == "Advanced Options":
        st.header("Advanced Options for Engaging Sophisticated Buyers")
        st.write("For brands prepared to take the next step, RippleXp offers advanced courses...")

    elif ripple_section == "Commercialization & Off-the-Shelf Products":
        st.header("Commercialization & Off-the-Shelf Products")
        st.write("RippleXp offers modular, off-the-shelf products that cater to brands...")

    elif ripple_section == "Crisis Identification Stages":
        st.header("Crisis Identification Stages - From Fear to Proactivity")
        st.write("Each RippleXp course addresses a critical stage in crisis management...")

    elif ripple_section == "Course Assessment":
        st.header("Course Assessment - Customized Recommendations")
        st.write("Our assessment tool helps clients identify the most relevant RippleXp courses...")

    # Footer CTA for RippleXp Courses
    st.write("---")
    st.write("Ready to secure your brand’s reputation? Start your RippleXp journey and prepare for RippleXn’s comprehensive monitoring services.")
    st.button("Contact Us for a Free Consultation")

# Keep the rest of your existing sections for Freemium Content, Premium Content, etc.
