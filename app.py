import streamlit as st

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
    "Course Tutors",
    "Courses"
])
# Content Ideas Section
if section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Manage your content ideas and track their completion status.")
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
    calendar_df = pd.DataFrame({"Date": dates[:len(tasks)], "Task": tasks, "Type": task_types})
    st.dataframe(calendar_df, use_container_width=True)

# Section: Viral Strategies
elif section == "Viral Strategies":
    st.header("Viral Strategies")
    st.write("Explore strategies to make your content go viral and maximize reach.")
    st.subheader("1. Utilize Hashtags Effectively")
    st.write("Research trending hashtags related to your industry or content theme. Use a mix of popular and niche hashtags to increase visibility and engagement.")
    st.subheader("2. Collaborate with Micro-Influencers")
    st.write("Partner with micro-influencers who have a highly engaged audience. Offering them exclusive freemium content can create buzz and increase your brand's reach.")
    st.subheader("3. Run Contests or Giveaways")
    st.write("Organize contests where followers share your content or tag friends. This encourages engagement and spreads your content organically.")
    st.subheader("4. Create Interactive Content")
    st.write("Use polls, quizzes, and Q&A sessions on platforms like Instagram Stories and LinkedIn. Interactive content boosts visibility and engagement.")
    st.subheader("5. Leverage Email Marketing")
    st.write("Send engaging email updates to your subscribers about your latest content. Encourage them to share it, and include a clear call to action.")

# SEO Strategy Section
elif section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy to maximize reach.")

# Notes & To-Do Section
elif section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your notes and tasks.")

# Links & Resources Section
elif section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful links and resources for influencer marketing.")

# Course Tutors Section
elif section == "Course Tutors":
    st.header("Course Tutors")
    st.write("Learn from our expert speakers, each specializing in a unique aspect of brand reputation and storytelling:")
    
    # Improved layout using columns
    st.markdown("---")
    
    # Building Confidence
    col1, col2 = st.columns([1, 3])
    with col1:
        # st.image("path_to_kay_image.jpg", use_column_width=True)  # Uncomment and replace with a valid image path
        pass
    with col2:
        st.subheader("Building Confidence")
        st.write("**Instructor:** Kay Munday")
        st.write("Kay Munday is an expert in helping professionals build confidence and presence in high-stakes situations. With years of experience in leadership coaching and public speaking, Kay has transformed countless professionals into confident, compelling communicators.")
    
    st.markdown("---")

    # Storytelling Narrative
    col1, col2 = st.columns([1, 3])
    with col1:
        # st.image("path_to_james_image.jpg", use_column_width=True)  # Uncomment and replace with a valid image path
        pass
    with col2:
        st.subheader("Storytelling Narrative")
        st.write("**Instructor:** Dr. James McCabe")
        st.write("Dr. James McCabe explores the art of storytelling as a strategic tool for brands. His sessions dive deep into crafting narratives that control and elevate brand reputation, making complex concepts accessible and actionable.")
    
    st.markdown("---")

    # Rhetoric
    col1, col2 = st.columns([1, 3])
    with col1:
        # st.image("path_to_brian_image.jpg", use_column_width=True)  # Uncomment and replace with a valid image path
        pass
    with col2:
        st.subheader("Rhetoric")
        st.write("**Instructor:** Brian Jenner")
        st.write("Brian Jenner specializes in the power of rhetoric, teaching professionals how to use persuasive language to influence and engage audiences effectively.")

# New Courses Section
elif section == "Courses":
    st.header("Courses")
    
    # Reputation Course Section
    st.subheader("Reputation - RippleXp")
    
    # Powerful Intro - "Why Now" and Calling Card Message
    st.write("""
        ### Why Now?
        In a world where brands are constantly under the lens, the fear of reputational damage has never been more palpable. 
        **RippleXp** serves as a calling card, capitalizing on this urgency by empowering brands to understand and manage the 
        multiple narratives surrounding them online. By leveraging the fear of reputational damage, RippleXp offers a gateway 
        to RippleXn's deeper social listening and reputation management services.
        
        Our approach is simple but powerful: use storytelling to uncover hidden risks and opportunities, allowing brands to 
        engage in self-reflection and proactive management. Through dedicated, hands-on courses, RippleXp equips teams with 
        the insights and skills they need to navigate today's high-stakes media landscape. **The Trojan horse?** RippleXp 
        positions brands to embrace RippleXn's full suite of social listening tools for ongoing protection.
    """)
    st.write("---")

    # Course Navigation for Reputation
    course_section = st.radio("Course Navigation", [
        "Overview", 
        "The RippleXp Approach", 
        "Target Audiences", 
        "Entry-Level Products", 
        "Advanced Options", 
        "Commercialization & Off-the-Shelf Products", 
        "Crisis Identification Stages", 
        "Course Assessment"
    ])

    # Content for Each Subsection
    if course_section == "Overview":
        st.header("Overview: RippleXp as a Top-of-Funnel Approach")
        st.write("""
            RippleXp acts as a strategic top-of-funnel entry point for RippleXn's core offerings. By engaging clients through storytelling 
            and reputation management courses, we position RippleXn's deeper social listening services as the logical next step.
        """)
        st.subheader("Key Objectives:")
        st.write("""
            - **Leverage Fear of Reputational Damage**: RippleXp addresses brand vulnerability head-on, sparking interest through actionable insights.
            - **Drive Discovery through Storytelling**: Courses are structured to teach clients the art of storytelling while subtly preparing them for RippleXn.
            - **Facilitate Smooth Transitions**: Graduates of RippleXp's courses are primed for more advanced reputation management services.
        """)

    elif course_section == "The RippleXp Approach":
        st.header("The RippleXp Approach to Reputation Management")
        st.write("""
            Reputation is a mosaic, composed of hundreds of individual stories that, together, create a brand's narrative. RippleXp's courses guide 
            clients through the storytelling process, uncovering hidden risks and opportunities that align with RippleXn's proactive listening 
            tools.
        """)
        st.subheader("Why Storytelling?")
        st.write("""
            Storytelling is not just a creative exercise; it's a strategic tool that allows brands to manage their narratives with intention.
            RippleXp helps brands develop the storytelling skills to navigate and control their reputation, leading naturally to the need 
            for RippleXn's advanced social listening solutions.
        """)

    elif course_section == "Target Audiences":
        st.header("Target Audiences - Four Key Areas of Focus")
        st.write("""
            RippleXp courses are tailored to address the different stages of brand audience engagement:
            
            - **No Audience Yet**: Brands looking to attract listeners and engage emerging trends.
            - **Existing Audience**: Brands with a current audience but lacking insight into competitive influences.
            - **Lost Audience (Crisis Management)**: Brands needing real-time recovery tactics.
            - **Other Voices Speaking**: Brands with influencers or advocates requiring training in brand representation.
        """)
        st.write("---")

    elif course_section == "Entry-Level Products":
        st.header("Entry-Level Products for Customer Acquisition")
        st.write("""
            These offerings serve as introductory tools to bring clients into the RippleXp ecosystem while priming them for RippleXn:
            
            - **$49 FTC/SEC Disclosure Training**: Ensures influencers meet regulatory standards, reducing risk.
            - **$75 Trend Analysis**: 100 hours of curated insights, highlighting key trends.
            - **$199 Risk & Strategy Support**: Choose between an influencer background check or a custom listening strategy.
        """)
        st.subheader("Course Delivery Options")
        st.write("""
            - **Half-Day Workshop**: Brief training sessions focused on immediate insights and regulatory basics.
        """)

    elif course_section == "Advanced Options":
        st.header("Advanced Options for Engaging Sophisticated Buyers")
        st.write("""
            For brands prepared to take the next step, RippleXp offers advanced courses that lead into RippleXn's ongoing monitoring services:
            
            - **Storytelling Courses**: Develop narrative skills for brand control.
            - **Social Video Alerts**: Real-time insights identifying emerging risks like greenwashing.
        """)
        st.subheader("Course Delivery Options")
        st.write("""
            - **Full-Day Workshop**: Intensive storytelling and brand reputation sessions.
            - **3-Day Immersive**: In-depth courses with hands-on application and strategy development.
        """)

    elif course_section == "Commercialization & Off-the-Shelf Products":
        st.header("Commercialization & Off-the-Shelf Products")
        st.write("""
            RippleXp offers modular, off-the-shelf products that cater to brands at various stages of crisis management and 
            audience engagement:
            
            - **Crisis Identification Products**: Scalable solutions that highlight brand vulnerabilities.
            - **Audience Insight Tools**: Pre-packaged courses that guide brands through common pitfalls.
            - **Advanced Monitoring Solutions**: RippleXn's full-service offerings for real-time brand listening.
        """)

    elif course_section == "Crisis Identification Stages":
        st.header("Crisis Identification Stages - From Fear to Proactivity")
        st.write("""
            Each RippleXp course addresses a critical stage in crisis management, from early detection to response. 
            We position RippleXp courses as essential tools for understanding where and how reputational threats emerge.
            
            - **Stage 1**: Identify reputation risks.
            - **Stage 2**: Address complications and educate through storytelling.
            - **Stage 3**: Engage ongoing RippleXn monitoring services for continued reputation management.
        """)

    elif course_section == "Course Assessment":
        st.header("Course Assessment - Customized Recommendations")
        st.write("""
            Our assessment tool helps clients identify the most relevant RippleXp courses based on their brand's unique needs, 
            guiding them seamlessly into the RippleXn ecosystem.
        """)
        st.subheader("Choose Your Path:")
        st.write("""
            - **Introductory Assessment**: Determine your starting point.
            - **Advanced Analysis**: For brands needing immediate intervention.
        """)

# Footer CTA
st.write("---")
st.write("Ready to secure your brand's reputation? Start your RippleXp journey and prepare for RippleXn's comprehensive monitoring services.")
st.button("Contact Us for a Free Consultation")
