import streamlit as st

# Tworzenie sidebaru do nawigacji
selected_page = st.sidebar.radio("Wybierz stronę:", [
    "Let's start here - Welcome! 🙌",
    "LearningApp - Titanic! 🚢",
    "LearningApp - Company! 🏢",
    "LookingApp - Friends! 🕵️‍♀️",
    "SwitchingApp - Marathon! 🏃‍♂️"
])

# Prosta logika dla przełączania stron
if selected_page == "Let's start here - Welcome! 🙌":
    import main_page
    main_page.run()
elif selected_page == "LearningApp - Titanic! 🚢":
    import titanic
    titanic.run()
elif selected_page == "LearningApp - Company! 🏢":
    import company
    company.run()
elif selected_page == "LookingApp - Friends! 🕵️‍♀️":
    import survey.finding_friends as finding_friends
    finding_friends.run()
elif selected_page == "SwitchingApp - Marathon! 🏃‍♂️":
    import marathon
    marathon.run()
