import streamlit as st
import importlib

# Definicja stron jako moduły
pages = {
    "Let's start here - Welcome! 🙌": "main_page.main_page",
    "LearningApp - Titanic! 🚢": "titanic.titanic",
    "LearningApp - Company! 🏢": "company.company",
    "LookingApp - Friends! 🕵️‍♀️": "survey.finding_friends",
    "SwitchingApp - Marathon! 🏃‍♂️": "marathon.marathon"
}

# Nawigacja w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Dynamiczne ładowanie modułu i uruchomienie funkcji `run()`
module_name = pages[selected_page]
module = importlib.import_module(module_name)
module.run()
