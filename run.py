import streamlit as st

# Definicja stron
pages = {
    "Let's start here - Welcome! 🙌": "main_page",
    "LearningApp - Titanic! 🚢": "titanic",
    "LearningApp - Company! 🏢": "company",
    "LookingApp - Friends! 🕵️‍♀️": "survey.finding_friends",
    "SwitchingApp - Marathon! 🏃‍♂️": "marathon"
}

# Nawigacja w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Importowanie i uruchamianie odpowiedniego modułu
if selected_page in pages:
    module = __import__(pages[selected_page])
    module.run()
