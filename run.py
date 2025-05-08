import streamlit as st
import importlib

# Definicja stron jako moduły
pages = {
    "Let's start here - Welcome! 🙌": "main_page",
    "LearningApp - Titanic! 🚢": "titanic",
    "LearningApp - Company! 🏢": "company",
    "LookingApp - Friends! 🕵️‍♀️": "survey.finding_friends",
    "SwitchingApp - Marathon! 🏃‍♂️": "marathon"
}

# Tworzenie nawigacji w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Zamiast `st.navigation(pages).run()`, używamy dynamicznego importowania
module = importlib.import_module(pages[selected_page])
module.run()
