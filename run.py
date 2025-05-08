import streamlit as st

# Importujemy moduły statycznie
from main_page import main_page/main_page.py
from titanic import titanic/titanic.py
from company import company.py
from survey import finding_friends
from marathon import marathon

# Tworzymy słownik ze stronami i ich powiązanymi funkcjami
pages = {
    "Let's start here - Welcome! 🙌": main_page.run,
    "LearningApp - Titanic! 🚢": titanic.run,
    "LearningApp - Company! 🏢": company.run,
    "LookingApp - Friends! 🕵️‍♀️": finding_friends.run,
    "SwitchingApp - Marathon! 🏃‍♂️": marathon.run
}

# Tworzenie nawigacji w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Wywołanie wybranej strony
pages[selected_page]()
