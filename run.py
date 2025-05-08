import streamlit as st

# Definicja stron jako funkcji
def main_page():
    st.title("Let's start here - Welcome! 🙌")
    st.write("To jest strona startowa.")

def titanic():
    st.title("LearningApp - Titanic! 🚢")
    st.write("Analiza danych pasażerów Titanica.")

def company():
    st.title("LearningApp - Company! 🏢")
    st.write("Dane dotyczące firm.")

def finding_friends():
    st.title("LookingApp - Friends! 🕵️‍♀️")
    st.write("Analiza ankiety dotyczącej znajomości.")

def marathon():
    st.title("SwitchingApp - Marathon! 🏃‍♂️")
    st.write("Informacje o maratonie.")

# Słownik stron
pages = {
    "Let's start here - Welcome! 🙌": main_page,
    "LearningApp - Titanic! 🚢": titanic,
    "LearningApp - Company! 🏢": company,
    "LookingApp - Friends! 🕵️‍♀️": finding_friends,
    "SwitchingApp - Marathon! 🏃‍♂️": marathon,
}

# Nawigacja w sidebarze
selected_page = st.sidebar.selectbox("Wybierz stronę", list(pages.keys()))

# Wywołanie odpowiedniej funkcji
pages[selected_page]()
