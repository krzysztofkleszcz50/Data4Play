import streamlit as st

# Correct imports for the respective modules
from main_page import main_page
from titanic import titanic
from company import company
from survey import finding_friends
from marathon import marathon

# Dictionary mapping pages to their respective functions
pages = {
    "Let's start here - Welcome! 🙌": main_page.py,
    "LearningApp - Titanic! 🚢": titanic.run,
    "LearningApp - Company! 🏢": company.run,
    "LookingApp - Friends! 🕵️‍♀️": finding_friends.run,
    "SwitchingApp - Marathon! 🏃‍♂️": marathon.run
}

# Sidebar navigation for selecting a page
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Execute the selected page function
pages[selected_page]()
