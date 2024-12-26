import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.header('SwitchingApp - Marathon! 🏃‍♂️')

# Wczytywanie danych
df = pd.read_csv("marathon/halfmarathon_wroclaw_2024__final_updated.csv", sep=";")

# Sidebar z filtrami
with st.sidebar:
    name = st.text_input("Name")
    cities = st.multiselect('City', sorted(df["Miasto"].dropna().unique()))
    age_categories = st.multiselect('Age', sorted(df["Kategoria wiekowa"].dropna().unique()))
    gender = st.radio("Sex", ["All", "Males", "Females"])

# Filtrowanie danych
if cities:
    df = df[df["Miasto"].isin(cities)]
if age_categories:
    df = df[df["Kategoria wiekowa"].isin(age_categories)]
if name:
    df = df[df["Imię"].str.contains(name, case=False)]
if gender == "Mężczyźni":
    df = df[df["Płeć"] == "M"]
elif gender == "Kobiety":
    df = df[df["Płeć"] == "K"]

# Sprawdzenie, czy DataFrame nie jest pusty
if not df.empty:
    # Liczba zawodników
    c0, c1, c2 = st.columns(3)
    with c0:
        st.metric("All people 👨👩", df.shape[0])
    with c1:
        st.metric("Males 👨", df[df["Płeć"] == "M"].shape[0])
    with c2:
        st.metric("Females 👩", df[df["Płeć"] == "K"].shape[0])

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Data overview 📝", "Histogram 📈", "Boxplot 📊", "Barplot 📊", "Scatterplot 📈", "Pie Chart 🌎"])

    with tab1:
        x = min(10, len(df))
        st.dataframe(df.sample(x).style.format(precision=2), use_container_width=True, hide_index=True)

    with tab2:
        # Histogram of running tempo
        fig = px.histogram(df, x='Tempo', nbins=30, title='Distribution of Running Tempo', color_discrete_sequence=['skyblue'])
        fig.update_layout(xaxis_title='Tempo (minutes per kilometer)', yaxis_title='Frequency')
        st.plotly_chart(fig)

    with tab3:
        # Boxplot of running tempo by gender
        fig = px.box(df, x='Płeć', y='Tempo', color='Płeć', title='Tempo by Gender', notched=True)
        fig.update_layout(xaxis_title='Gender', yaxis_title='Tempo (minutes per kilometer)')
        st.plotly_chart(fig)

    with tab4:
        # Bar plot of average tempo by gender
        df_cleaned = df.dropna(subset=['Płeć', 'Tempo'])
        average_tempo_by_gender = df_cleaned.groupby('Płeć')['Tempo'].mean().reset_index()
        fig = px.bar(average_tempo_by_gender, x='Płeć', y='Tempo', color='Płeć', title='Average Tempo by Gender', text='Tempo')
        fig.update_layout(xaxis_title='Gender', yaxis_title='Average Tempo (minutes per kilometer)')
        st.plotly_chart(fig)

    with tab5:
        # Scatterplot of tempo vs. age category (cleaned data)
        df_cleaned = df.dropna(subset=['Tempo'])
        fig = px.scatter(df_cleaned, x='Kategoria wiekowa', y='Tempo', color='Płeć', title='Tempo vs. Age Category', size='Tempo', hover_data=['Imię'])
        fig.update_layout(xaxis_title='Age Category', yaxis_title='Tempo (minutes per kilometer)')
        st.plotly_chart(fig)

    with tab6:
        # Pie chart of participants by country
        df_filtered = df[df['Kraj'] != 'POL']
        country_counts = df_filtered['Kraj'].value_counts().reset_index()
        country_counts.columns = ['Country', 'Count']
        fig = px.pie(country_counts, names='Country', values='Count', title='Participants by Country (excluding Poland)')
        fig.update_traces(textinfo='none')
        st.plotly_chart(fig)

else:
    st.write("Brak danych do wyświetlenia po zastosowaniu filtrów.")
