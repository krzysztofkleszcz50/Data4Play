import streamlit as st

# Definicja stron
pages = {
    "Let's start here - Welcome! 🙌": "main_page/main_page.py",
    "LearningApp - Titanic! 🚢": "titanic/titanic.py",
    "LearningApp - Company! 🏢": "company/company.py",
    "LookingApp - Friends! 🕵️‍♀️": "survey/finding_friends.py",
    "SwitchingApp - Marathon! 🏃‍♂️": "marathon/marathon.py"
}

# Tworzenie nawigacji w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Załadowanie wybranej strony
st.write(f"Ładowanie: {selected_page}")
exec(open(pages[selected_page]).read())
