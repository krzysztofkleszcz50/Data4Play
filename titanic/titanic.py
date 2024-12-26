import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pycaret.classification import load_model, predict_model
import base64

mode = st.sidebar.radio("Choose your mode 🧭", ['Introduction ✨', 'Machine learning ⌛', 'Data analysis 🔍', 'Presentation 📂'])

if mode == 'Introduction ✨':
    
    st.title("LearningApp - Titanic! 🚢")
    st.write("""
             
    **Join me in exploring titanic analysis! 😀**
    \n Please see menu at the sidebar on the left side. 
    \n Discover titanic dataset - it will be interesting, yes! 
    \n My application offers ✨:

    - **Model Classification**: You can add passenger details and check his survival chances. 
    - **In-Depth Data Analysis**: You can see data analysis in nice form. 
    - **Various Presentation Options**: Slides, Articles, Notebooks.

    Whether you prefer model classification, data analysis or presentation? 📚
    \n This app has all the resources you need 😉
    """)

if mode == 'Machine learning ⌛':

    st.title("Machine learning 👓")

    tab1, tab2, tab3 = st.tabs(["Introduction ✔", "Values input 🔍", "Key feature 💎"])

    with tab1:
        st.header("Machine learning introduction 💡")
        st.write("""\n In this session, we will focus on survive chances classification. 
                    \n You can even check if this model has right! 
                    \n To do this, please see Data analysis section. 
                    \n To start this epic journey, please click tab **Values input 😉**""")

    with tab2:
        MODEL_NAME_3 = 'titanic/titanic_classification_pipeline_v2'

        @st.cache_data
        def load_classification_model():
            return load_model(MODEL_NAME_3)

        model = load_classification_model()

        def classify_survived(input_data):
            # Data transformacion
            input_data['Sex'] = 1 if input_data['Sex'] == 'male' else 0
            input_data['Embarked'] = 0 if input_data['Embarked'] == 'C' else (1 if input_data['Embarked'] == 'Q' else 2)
            
            input_df = pd.DataFrame([input_data])
            predictions = predict_model(model, data=input_df)
            return predictions

        st.header("Please add passenger data: 📚")
        passenger_class = st.selectbox("Class", [1, 2, 3])
        sex = st.selectbox("Sex", ["male", "female"])
        age = st.number_input("Age", min_value=0, max_value=100, value=30)
        sibsp = st.number_input("Family (execpt parents/childrens)", min_value=0, max_value=10, value=0)
        parch = st.number_input("Parents/childrens", min_value=0, max_value=10, value=0)
        fare = st.number_input("Fare", min_value=0.0, max_value=1000.0, value=50.0)
        embarked = st.selectbox("Starting port", ["C", "Q", "S"])

        input_data = {
            'Pclass': passenger_class,
            'Sex': sex,
            'Age': age,
            'SibSp': sibsp,
            'Parch': parch,
            'Fare': fare,
            'Embarked': embarked
        }

        if st.button("Check survive chances"):
            result = classify_survived(input_data)
            st.write(f"**Survival chances:** {result['prediction_label'].values[0]}")

    with tab3:    
        st.title('Key feature 🔑')

        st.image('titanic/key_feature2.PNG', caption='key_feauture', use_column_width=True)

if mode == 'Data analysis 🔍':

    st.title("Data analysis 🔎")

    with st.expander("Bored? 😉 Check summary then! 🔍"):
        st.write("""
                    * The data turned out to be more difficult due to many missing values.
                    * This led to data transformation by calculating averages or transforming columns.
                    * We can observe that nearly every woman in first and second class survived.
                    * The highest chances of survival were for those who embarked from port C.
                    * We can observe that the more expensive the ticket, the higher the chance of survival.
                    * The most outliers were found in the first class, specifically regarding ticket prices.
                """)

    # Ładowanie danych i zmiana nazw kolumn
    df = pd.read_csv('titanic/titanic.csv')
    df.columns = ['pclass', 'survived', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest']

    # Usunięcie kolumn tekstowych, które mogą powodować błędy
    df = df.drop(columns=['name', 'ticket', 'cabin', 'boat', 'body', 'home.dest'])

    # Konwersja danych tekstowych na numeryczne
    df['sex'] = df['sex'].apply(lambda x: 1 if x == 'male' else 0)
    df['embarked'] = df['embarked'].apply(lambda x: 0 if x == 'C' else (1 if x == 'Q' else 2))

    # Przełączanie między zakładkami
    tab1, tab2, tab3 = st.tabs(["Data Overview 📕", "Histogram 📈", "Correlations 📊"])

    with tab1:
        st.write("""We can observe that we have very diverse data, including both textual and numerical values. It's
                    important to note that we also have missing parameters.""")
        st.write(df.sample(10))

    with tab2:
        options = ["Pclass", "Age", "Fare", "Parch"] 
        choice = st.select_slider("Choose your histogram:", options=options)

        if choice == "Pclass":
            st.write("Most part of passenger had third clase.")
            fig = plt.figure(figsize=(8, 3))
            plt.hist(df['pclass'], bins=20, color='skyblue', edgecolor='black')
            plt.title('Histogram of pclass')
            plt.xlabel('pclass')
            plt.ylabel('Frequency')
            st.pyplot(fig)

        if choice == "Age":
            st.write("Most part of passenger was young.")
            fig = plt.figure(figsize=(8, 3))
            plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
            plt.title('Histogram of age')
            plt.xlabel('age')
            plt.ylabel('Frequency')
            st.pyplot(fig)

        if choice == "Fare":
            st.write("Most part of fare was cheap.")
            fig = plt.figure(figsize=(8, 3))
            plt.hist(df['fare'], bins=20, color='skyblue', edgecolor='black')
            plt.title('Histogram of fare')
            plt.xlabel('fare')
            plt.ylabel('Frequency')
            st.pyplot(fig)

        if choice == "Parch":
            st.write("Most part of passenger travelled alone.")
            fig = plt.figure(figsize=(8, 3))
            plt.hist(df['parch'], bins=20, color='skyblue', edgecolor='black')
            plt.title('Histogram of parch')
            plt.xlabel('parch')
            plt.ylabel('Frequency')
            st.pyplot(fig)

    with tab3:
        options = ["Matrix1", "Matrix2", "Matrix3", "Scatterplot"] 
        choice = st.select_slider("Choose your histogram:", options=options)
        if choice == "Matrix1":
            st.write("We can observe that nearly every woman in first and second class survived. On the other hand, far fewer men survived compared to women.")
            survival_rates = df.groupby(['pclass', 'sex'])['survived'].mean().reset_index()
            pivot_table = survival_rates.pivot(index='pclass', columns='sex', values='survived')
            plt.figure(figsize=(10, 4))
            sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Survival Rate'})
            plt.title('Survival Rates by Class and Gender')
            plt.xlabel('Gender')
            plt.ylabel('Class')
            plt.xticks(rotation=45)
            plt.yticks(rotation=0)
            st.pyplot(plt.gcf())

        if choice == "Matrix2":
            st.write("The highest chances of survival were for those who embarked from port C. 🚢")
            survival_rates = df.groupby(['pclass', 'embarked'])['survived'].mean().reset_index()
            pivot_table = survival_rates.pivot(index='pclass', columns='embarked', values='survived')
            plt.figure(figsize=(10, 4))
            sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Survibval Rate'})
            plt.title('Survival Rates by Class and Embarked')
            plt.xlabel('Embarked')
            plt.ylabel('Class')
            plt.xticks(rotation=45)
            plt.yticks(rotation=0)
            st.pyplot(plt.gcf())

        if choice == "Matrix3":
            st.write("We can see some correlations in this matrix. More blue boxes has bigger impact.")
            matrix = df.corr()
            colormap = sns.light_palette("blue", as_cmap=True)
            matrix_colored = matrix.style.background_gradient(cmap=colormap)
            st.dataframe(matrix_colored)
        if choice == "Scatterplot":
            st.write("Correlation between age and fare. It is difficult to notice some pattern here.")
            plt.figure(figsize=(10, 6))
            scatter = sns.scatterplot(x='fare', y='age', hue='survived', data=df)
            st.pyplot(plt.gcf())

if mode == 'Presentation 📂':
    
    tab1, tab2, tab3 = st.tabs(["Slides 📂", "Article 📂", "Notebook 📂"])

    with tab1:
        st.title('Titanic! - Presentation 💻')
        presentation_path = "titanic/titanic_slides.pdf"

        try:
            with open(presentation_path, "rb") as file:
                notebook_content = file.read()

            st.download_button(
                label="Download titanic_presentation.pdf",
                data=notebook_content,
                file_name="titanic_slides.pdf",
                mime="application/pdf"
            )
        except FileNotFoundError:
            st.error(f"Plik {presentation_path} nie został znaleziony. Upewnij się, że plik znajduje się w odpowiedniej lokalizacji.")

        with tab2:
            st.title('Titanic! - Article 📢')
            presentation_path = "titanic/titanic_pdf.pdf"

            try:
                with open(presentation_path, "rb") as file:
                    notebook_content = file.read()

                st.download_button(
                    label="Download titanic_Article.pdf",
                    data=notebook_content,
                    file_name="titanic_Article.pdf",
                    mime="application/pdf"
                )
            except FileNotFoundError:
                st.error(f"Plik {presentation_path} nie został znaleziony. Upewnij się, że plik znajduje się w odpowiedniej lokalizacji.")


        with tab3:
             
            st.title('Titanic! - Notebook ⛳')

            notebook_path = "titanic/titanic.ipynb"

            with open(notebook_path, 'r', encoding='utf-8') as file:
                notebook_content = file.read()

            st.download_button(
                label="Download titanic.ipynb",
                data=notebook_content,
                file_name="titanic.ipynb",
                mime="application/octet-stream"
            )
