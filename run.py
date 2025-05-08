import streamlit as st

# Definicja stron jako funkcji
def main_page():
    st.write("Let's start here - Welcome! 🙌": "main_page/main_page.py")

def titanic():
    st.title("LearningApp - Titanic! 🚢")

def company():
    st.title("LearningApp - Company! 🏢")

def finding_friends():
    st.title("LookingApp - Friends! 🕵️‍♀️")

def marathon():
    st.title("SwitchingApp - Marathon! 🏃‍♂️")

# Słownik stron
pages = {
    "Let's start here - Welcome! 🙌": main page
    "LearningApp - Titanic! 🚢": titanic
    "LearningApp - Company! 🏢": company,
    "LookingApp - Friends! 🕵️‍♀️": finding_friends,
    "SwitchingApp - Marathon! 🏃‍♂️": marathon,
}

# Nawigacja w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Wywołanie odpowiedniej funkcji
pages[selected_page]()
