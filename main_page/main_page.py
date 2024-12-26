import streamlit as st

tab1, tab2 = st.tabs(["**Data4Play 💻**", "**MySkills! 💎**"])

with tab1:
    st.write("""

    ### Welcome to Data4Play! 😊

    Also show you interactive analysis. 📈 
    \n My app offers four interactive data analysis:
    - **Titanic analyse** 🚢
    - **CD Projekt Analyse** 🏢
    - **Survey analyse** 🕵️‍♂️
    - **Marathon analyse** 🏃‍♂️

    This applications reflects my knowledge in this dynamic field. 

    I invite you to explore the projects and welcome any questions or feedback you may have. 
    \n **Thank you for visiting Data4Play! 😀✨**
    """)

with tab2:
    st.write("""
    ### MySkills! 💎
    \n Skills, which I present in this application:
    - **Python** (functions, logics, streamlit) 🦎
    - **Data processing** (pandas, matplotlib, seaborn) 📈
    - **Machine Learning** (Pycaret, classification) 🧭
    - **Deploying** 📝
    """)

