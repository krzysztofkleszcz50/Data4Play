import streamlit as st 
pages = { "Data4Play 💻": [ st.Page("main_page/main_page.py", title="Let's start here - Welcome! 🙌"), st.Page("titanic/titanic.py", title="LearningApp - Titanic! 🚢"), st.Page("company/company.py", title="LearningApp - Company! 🏢"), st.Page("survey/finding_friends.py", title="LookingApp - Friends! 🕵️‍♀️"), st.Page("marathon/marathon.py", title="SwitchingApp - Marathon! 🏃‍♂️") ], } 
pg = st.navigation(pages) 
pg.run()
