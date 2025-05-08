import streamlit as st
import importlib

# Tworzymy słownik ze stronami
pages = {
    "Let's start here - Welcome! 🙌": "main_page.main_page",
    "LearningApp - Titanic! 🚢": "titanic.titanic",
    "LearningApp - Company! 🏢": "company.company",
    "LookingApp - Friends! 🕵️‍♀️": "survey.finding_friends",
    "SwitchingApp - Marathon! 🏃‍♂️": "marathon.marathon"
}

# Tworzenie nawigacji w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Dynamiczne ładowanie modułu
module_name = pages[selected_page]
module = importlib.import_module(module_name)
module.run()
