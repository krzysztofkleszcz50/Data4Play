import streamlit as st

# Funkcja definiująca strony
def main_page():
    st.title("Let's start here - Welcome! 🙌")
    st.write("Witamy na stronie głównej aplikacji Data4Play!")

def titanic_page():
    st.title("LearningApp - Titanic! 🚢")
    st.write("Tutaj znajdziesz analizę danych dla Titanica.")

def company_page():
    st.title("Company Analysis")
    st.write("Tutaj znajdziesz informacje o firmie.")

# Słownik stron
pages = {
    "Data4Play 💻": main_page,
    "LearningApp - Titanic! 🚢": titanic_page,
    "Company Analysis": company_page,
}

# Pasek nawigacyjny
st.sidebar.title("Nawigacja")
selected_page = st.sidebar.radio("Wybierz stronę", list(pages.keys()))

# Wywołanie wybranej strony
pages[selected_page]()
