import streamlit as st

# Page configuration
st.set_page_config(page_title="RippleXp Content Dashboard", layout="wide")

# Home Page
st.title("RippleXp Content Management Dashboard")
st.subheader("Manage your content ideas efficiently.")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Content Ideas", "SEO Strategy", "Notes & To-Do", "Links & Resources"])

# Page Sections
if section == "Home":
    st.write("Welcome to the RippleXp Content Management Dashboard!")

elif section == "Content Ideas":
    st.header("Content Ideas")
    st.write("Here you can manage your content ideas.")

elif section == "SEO Strategy":
    st.header("SEO Strategy")
    st.write("Plan your SEO strategy here.")

elif section == "Notes & To-Do":
    st.header("Notes & To-Do")
    st.write("Keep track of your tasks and notes.")

elif section == "Links & Resources":
    st.header("Links & Resources")
    st.write("Access useful resources here.")
