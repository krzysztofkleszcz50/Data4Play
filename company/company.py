#Code structure
#1. Imports
#2. Modes
#3. Introduction
#4. Finance analyse
#5. Ratio analyse
#6. Strategy analyse
#7. Conlcusion

#Import
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#Modes
mode = st.sidebar.radio("Wybierz rozdział 📗", ['Wstęp 📝', "Analiza sprawozdań 📈", "Analiza wskaźników 📊", "Analiza strategii 🧭", "Podsumowanie 💎"])

#Wstęp
if mode == 'Wstęp 📝':
    st.title("Ogólne informacje 👓")
    tab1, tab2, tab3, tab4 = st.tabs(["Wstęp 📌", "Ogólne 📘", "Struktura 🧰", "Produkty 💻"])
    with tab1:
        st.write("""Konwertowanie pracy magisterskiej do aplikacji? **Obowiązkowo!** 😮
                    \n Tylko że tym razem **w przystępnej** dla każdego formie 😊
                    \n **No worries!** Nie będzie nudno 😉
                    \n Szykuj się na **apkonalizę** finansowo-strategiczną spółki CD Projekt! 😉 """)
    #Spis treści
        sections = [
            "Wstęp",
            "Analiza sprawozdań",
            "Analiza wskaźników",
            "Analiza strategii",
            "Podsumowanie"
        ]
        fig = go.Figure()
        #Sekcje wykresu
        for i, section in enumerate(sections):
            fig.add_trace(go.Scatter(
                x=[i],
                y=[1],
                mode="markers+text",
                marker=dict(size=40, color="lightblue"),
                text=section,
                textposition="top center"
            ))
        #Wygląd wykresu
        fig.update_layout(
            title="Spis Treści",
            showlegend=False,
            xaxis=dict(showticklabels=False, zeroline=False),
            yaxis=dict(showticklabels=False, zeroline=False),
            font=dict(size=16),
            width=800,
            height=400
        )
        #Wykres
        st.plotly_chart(fig)

    with tab2:
        st.write("""**Główny cel?** Tworzenie gier wideo, a dokładniej gier fabularnych!
                    \n**Główna siedziba?** Warszawa! Firma posiada oddziały na
                    całym świecie. 
                    \n**Ambicje?** Firma ma ambicje zdobyć miejsce w trójce
                    najlepszych producentów 😉""")
        # Najważniejsze wydarzenia
        events = [
            "Otwarcie",
            "Sklepu internetowego GOG.com",
            "Gra Wiedźmin 3"
        ]
        years = [1994, 2008, 2015]
        #Tworzenie grafu
        fig = go.Figure()
        #Wygląd wykresu
        fig.add_trace(go.Scatter(
            x=years,
            y=[1, 1, 1],
            mode="markers+text",
            marker=dict(size=20, color="lightblue"),
            text=events,
            textposition="top center"
        ))
        fig.update_layout(
            title="Kluczowe momenty dla CD Projekt",
            showlegend=False,
            xaxis=dict(title="Rok", tickvals=years),
            yaxis=dict(showticklabels=False),
            font=dict(size=14),
            width=800,
            height=400
        )
        #Wykres
        st.plotly_chart(fig)

    with tab3:
        st.write("""**Struktura?** Zarząd oraz Rada Nadzorcza. 
                    \n Do zadań zarządu należy reprezentowanie oraz prowadzenie danej Spółki. 
                    \n Z kolei do zadań Rady Nadzorczej
                    należy nadzorowanie działania Spółki. """)
        #Struktura
        nodes = [
            "Zarząd", "Prezes", "Wiceprezes", "Wiceprezes",
            "Rada Nadzorcza", "Członkowie"
        ]
        edges = [
            ("Zarząd", "Prezes"), ("Zarząd", "Wiceprezes"), ("Zarząd", "Wiceprezes"),
            ("Rada Nadzorcza", "Członkowie")
        ]
        #Wygląd wykresu
        fig = go.Figure()
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[nodes.index(node)], y=[1],
                mode="markers+text",
                marker=dict(size=40, color="lightblue"),
                text=node,
                textposition="top center"
            ))
        for edge in edges:
            fig.add_trace(go.Scatter(
                x=[nodes.index(edge[0]), nodes.index(edge[1])],
                y=[1, 1],
                mode="lines",
                line=dict(width=2, color="grey")
            ))
        fig.update_layout(
            title="Uproszczona struktura",
            showlegend=False,
            xaxis=dict(showticklabels=False, zeroline=False),
            yaxis=dict(showticklabels=False, zeroline=False),
            font=dict(size=16),
            width=800,
            height=400
        )
        #Wykres
        st.plotly_chart(fig)

        with tab4:
            st.write("""**Branża docelowa?** Branża elektronicznej rozrywki. 
                        \n Głównym produktem firmy CD Projekt są gry komputerowe. 
                        \n **Największa poularność?** Seria Wiedźmin! 
                        \n **Dodatkowa działalność?** - Platforma GOG.com umożliwiającą dystrybucję gier. 
                        """)
  
#Analiza sprawozdań
if mode == 'Analiza sprawozdań 📈':
    st.title("Analiza sprawozdań 🔍")
    tab1, tab2, tab3, tab4 = st.tabs(["Aktywa 📚", "Pasywa 📚", "Rachunek zysków i strat 📚", "Przepływy pieniężne 📚"])

    with tab1:
        options = ["Aktywa ogółem", "Wartości niematerialne i prawne", "Należności krótkoterminowe", "Inwestycje", "Podsumowanie"] 
        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Aktywa ogółem":
            st.write("""
                    W latach 2019-2021, można zauważyć przyrost
                    absolutny aktywów o 754 627 tys. zł. (aktywa zwiększyły się o 34,96%). Jednak największy
                    wzrost wartości aktywów można zauważyć w 2019 i 2020 roku.
            """)

        if choice == "Wartości niematerialne i prawne":
            st.write("""
                    Wartości niematerialne i prawne utrzymują się na wysokim poziomie w latach 2019-2021,
                    co jest istotne w przypadku spółki zajmującej się produkcją gier.
            """)

        if choice == "Należności krótkoterminowe":
            st.write("""
                    Pozycje, których współczynnik wzrostu był największy to należności krótkoterminowe oraz
                    środki pieniężne. Ma to odzwierciedlenie w tym, że CD Projekt w tym okresie zawierał nowe
                    umowy.
            """)

        if choice == "Inwestycje":
            st.write("""
                    Wśród inwestycji
                    długoterminowych oraz krótkoterminowych można zauważyć wyraźną tendencję wzrostową.
                    Przyrost absolutny inwestycji długoterminowych na przestrzeni lat 2019-2021 wynosił 213 063
                    tys. zł., natomiast w przypadku inwestycji krótkoterminowych wartość ta wynosiła 502 050 tys.
                    zł. 
            """)

        if choice == "Podsumowanie":
            st.write("""
                    Podsumowując, w 2020 roku spółka CD Projekt posiadała największą wartość aktywów
                    razem. Wskaźnik dynamiki wszystkich pozycji aktywów na przestrzeni lat 2019-
                    2021 wyniósł 153,74%, co pomimo spadku w roku 2020 wskazuje raczej na trend wzrostowy.
            """)
        #Dane do wykresu
        data = {
            "Kategoria": ["Aktywa trwałe", "Wartości niematerialne i prawne", "Rzeczowe składniki majątku trwałego", 
                        "Należności długoterminowe", "Inwestycje długoterminowe", "Pozostałe aktywa trwałe", 
                        "Aktywa obrotowe", "Zapasy", "Należności krótkoterminowe", "Inwestycje krótkoterminowe", 
                        "Środki pieniężne i inne aktywa pieniężne", "Pozostałe aktywa obrotowe"],
            "2019": [679097, 502049, 105267, 66321, 52985, 18730, 725011, 12862, 210292, 482301, 49406, 19556],
            "2020": [764178, 523026, 105349, 0, 120300, 15182, 2130300, 6957, 1275813, 834147, 563335, 13383],
            "2021": [905846, 465026, 115234, 686, 266048, 58852, 1252889, 15886, 238889, 984351, 411586, 13763]
        }

        df = pd.DataFrame(data)

        #Wygląd wykresu
        df_long = pd.melt(df, id_vars=["Kategoria"], var_name="Rok", value_name="Wartość")
        fig = px.bar(df_long, x="Kategoria", y="Wartość", color="Rok", barmode="group",
                    title="Analiza Aktywów CD Projekt w latach 2019-2021",
                    labels={"Kategoria": "Kategoria Aktywów", "Wartość": "Wartość (tys. PLN)", "Rok": "Rok"})
        st.plotly_chart(fig)

    with tab2:
        options = ["Kapitał", "Zobowiązania", "Podsumowanie"] 

        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Kapitał":
            st.write("""
                    W 2020 roku nastąpił
                    prawie dwukrotny wzrost kapitału własnego. Jest to związane z rozwojem firmy, co prowadzi
                    do zwiększonego zapotrzebowania na środki pieniężne. 
            """)

        if choice == "Zobowiązania":
            st.write("""
                    Można zauważyć wzrost zobowiązań
                    długoterminowych oraz zobowiązań krótkoterminowych w latach 2019-2020. Duży przyrost w zobowiązaniach spowodowany był
                    rozwojem firmy oraz pracą nad projektowaniem gry Cyberpunk 2077. 
            """)

        if choice == "Podsumowanie":
            st.write("""
                    Podsumowując, wszystkie pozycje pasywów na przestrzeni lat 2019-2021 wzrosły o
                    34,96%. Zobowiązania spółki w największej wartości utrzymywały się w roku 2020, kiedy to
                    spółka pracowała nad nową grą.
            """)
        #Dane do wykresu
        data = {
            "Kategoria": [
                "Kapitał własny akcjonariuszy", "Kapitał (fundusz) podstawowy", "Kapitał (fundusz) zapasowy", 
                "Zobowiązania długoterminowe", "Zobowiązania z tytułu leasingu finansowego", "Inne zobowiązania długoterminowe", 
                "Zobowiązania krótkoterminowe", "Z tytułu dostaw i usług", "Zobowiązania z tytułu leasingu finansowego", 
                "Inne zobowiązania krótkoterminowe",],
            "2019": [1105651, 96120, 780951, 25158, 17751, 7407, 273299, 59866, 2154, 211279],
            "2020": [2187356, 100655, 774851, 166153, 16006, 150147, 540969, 115444, 2933, 422592],
            "2021": [1894356, 100739, 1425647, 36112, 21080, 15032, 228267, 53380, 25802, 149085]
        }
        df = pd.DataFrame(data)
        #Wygląd wykresu
        df_long = pd.melt(df, id_vars=["Kategoria"], var_name="Rok", value_name="Wartość")
        fig = px.bar(df_long, x="Kategoria", y="Wartość", color="Rok", barmode="group",
                    title="Analiza Pasywów CD Projekt w latach 2019-2021",
                    labels={"Kategoria": "Kategoria Pasywów", "Wartość": "Wartość (tys. PLN)", "Rok": "Rok"})
        st.plotly_chart(fig)

    with tab3:
        options = ["Top 5", "Sprzedaż", "Koszty", "Podsumowanie"] 

        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Top 5":
            st.write("""
                    - Przychody ze sprzedaży, 
                    - Zysk ze sprzedaży,
                    - Zysk operacyjny, 
                    - Zysk z działalności gospodarczej,
                    - Zysk netto. 
            """)

        if choice == "Sprzedaż":
            st.write("""
                    Najwięcej przychodów ze sprzedaży pochodziło z działalności eksportowej. Wartość tych
                    przychodów w 2021 roku wynosiła 96,3%. 
            """)

        if choice == "Koszty":
            st.write("""
                    Wraz z rozwojem spółki, zwiększyły się też nakłady na tworzenie rezerw. Z kolei największą wartość w kosztach stanowiły odpisy aktualizujące wartość rzeczowych aktywów.
            """)

        if choice == "Podsumowanie":
            st.write("""
                    Największy udział w
                    przychodach operacyjnych miały dotacje oraz przychody z najmu. Zysk netto natomiast
                    zwiększył swoją wartość o 16,08% w badanym okresie. 
            """)
        #Dane do wykresu
        data = {
            "Kategoria": [
                "Przychody ze sprzedaży", "Techniczny koszt wytworzenia produkcji sprzedanej", "Koszty sprzedaży", 
                "Koszty ogólnego zarządu", "Zysk ze sprzedaży", "Pozostałe przychody operacyjne", "Pozostałe koszty operacyjne", 
                "Zysk operacyjny", "Przychody finansowe", "Koszty finansowe", "Zysk z działalności gospodarczej", "Zysk netto"
            ],
            "2019": [521272, 161308, 125341, 57113, 177510, 8279, 5503, 180286, 9463, 587, 189162, 175315],
            "2020": [2138875, 491364, 408016, 66435, 1173060, 8438, 24421, 1157077, 17081, 9209, 1164949, 1154327],
            "2021": [888172, 250234, 299225, 71949, 266764, 17370, 51231, 232903, 9523, 23318, 219108, 208908]
        }
        df = pd.DataFrame(data)
        #Wygląd wykresu
        df_long = pd.melt(df, id_vars=["Kategoria"], var_name="Rok", value_name="Wartość")
        fig = px.bar(df_long, x="Kategoria", y="Wartość", color="Rok", barmode="group",
                    title="Analiza Przychodów i Zysków CD Projekt w latach 2019-2021",
                    labels={"Kategoria": "Kategoria Finansowa", "Wartość": "Wartość (tys. PLN)", "Rok": "Rok"})
        st.plotly_chart(fig)

    with tab4:
        st.write("""
                Wśród najważniejszych pozycji tutaj można wyróżnić przepływy
                pieniężne z działalności operacyjnej, inwestycyjnej, finansowej oraz przypływy pieniężne
                razem. 
        """)
        #Dane do wykresu
        data = {
            "Kategoria": [
                "Przepływy pieniężne z działalności operacyjnej", "Amortyzacja", "Przepływy pieniężne z działalności inwestycyjnej", 
                "CAPEX (niematerialne i rzeczowe)", "Przepływy pieniężne z działalności finansowej", "Dywidenda", "Przepływy pieniężne razem"
            ],
            "2019": [216706, 37487, -164498, 293242, -107180, 100926, -54972],
            "2020": [711708, 267664, -106386, 221592, -91393, 0, 513929],
            "2021": [967825, 104729, -613795, 185455, -505779, 503694, -151749]
        }
        df = pd.DataFrame(data)
        #Wygląd wykresu
        df_long = pd.melt(df, id_vars=["Kategoria"], var_name="Rok", value_name="Wartość")
        fig = px.bar(df_long, x="Kategoria", y="Wartość", color="Rok", barmode="group",
                    title="Analiza Przepływów Pieniężnych CD Projekt w latach 2019-2021",
                    labels={"Kategoria": "Kategoria Finansowa", "Wartość": "Wartość (tys. PLN)", "Rok": "Rok"})
        st.plotly_chart(fig)

if mode == 'Analiza wskaźników 📊':

    st.title("Analiza wskaźników 💡")

    tab1, tab2 = st.tabs(["Wskaźniki płynności 📈", "Wskaźniki rentowności 📈"])

    with tab1:
        options = ["Pierwszy stopień pokrycia", "Drugi stopień pokrycia", "Kapitał pracujący", "Podsumowanie"] 
        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Pierwszy stopień pokrycia":
            st.write("""
                    Wskaźnik ten utrzymuje się wysoko powyżej wartości 1
                    w latach 2019-2021. Oznacza to bardzo mocną niezależność przedsiębiorstwa, gdyż
                    aktywa trwałe pokrywane są z wartości kapitałów własnych w bardzo dużym stopniu. 
            """)

        if choice == "Drugi stopień pokrycia":
            st.write("""
                    Wskaźnik ten też kształtuje się wysoko powyżej wartości 1,
                    co oznacza ustabilizowaną sytuację przedsiębiorstwa na rynku. Oznacza to bardzo
                    mocną niezależność przedsiębiorstwa, gdyż aktywa trwałe pokrywane są z wartości
                    kapitałów oraz zobowiązań długoterminowych w bardzo dużym stopniu. 
            """)

        if choice == "Kapitał pracujący":
            st.write("""
                    Wartość kapitału pracującego w przypadku spółki CD Projekt
                    wykazuje bardzo wysoką wartość. Oznacza to, że część kapitału stałego oraz
                    zobowiązań długoterminowych wpływa na finansowanie aktywów obrotowych.
            """)

        if choice == "Podsumowanie":
            st.write("""
                    Podsumowując wszystkie dotychczas przeanalizowane obliczenia, spółka CD Projekt
                    ma bardzo dobrą relację struktury pasywów do struktury aktywów. Wysokie wartości
                    wskaźników świadczą o korzystnej sytuacji finansowej spółki.
            """)
        #Dane do wykresu
        data = {
            "Wskaźniki": ["Pierwszy stopień pokrycia", "Drugi stopień pokrycia", "Kapitał pracujący/aktywa obrotowe"],
            "2019": [1.6281, 1.6652, 62.30],
            "2020": [2.8624, 3.0798, 74.61],
            "2021": [2.0913, 2.1311, 81.78]
        }
        df = pd.DataFrame(data)
        #Wygląd wykresu
        df_long = pd.melt(df, id_vars=["Wskaźniki"], var_name="Rok", value_name="Wartość")
        fig = px.bar(df_long, x="Wskaźniki", y="Wartość", color="Rok", barmode="group",
                    title="Wskaźniki Finansowe CD Projekt w latach 2019-2021",
                    labels={"Wskaźniki": "Wskaźniki Finansowe", "Wartość": "Wartość", "Rok": "Rok"})
        st.plotly_chart(fig)

    with tab2:
        options = ["Wskaźnik rentowności netto kapitału własnego", "Wskaźnik rentowności netto aktywów", "Wskaźnik rentowności netto sprzedaży"] 
        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Wskaźnik rentowności netto kapitału własnego":
            st.write("""
                    Wartość tego wskaźnika
                    gwałtownie wzrosła w 2020 roku i wynosiła o 36,91 punktów procentowych więcej niż
                    w 2019 roku. W 2020 roku spółce udało się wygenerować bardzo wysoką wartość zysku
                    z wniesionych kapitałów.             """)

        if choice == "Wskaźnik rentowności netto aktywów":
            st.write("""
                        Wartość tego wskaźnika osiągnęła swoje
                        maksimum w 2020 roku i była wyższa o niemal 40 procent od wartości z 2019 roku. Zdolność
                        spółki CD Projekt do generowania zysków była największa w 2020 roku. 
            """)

        if choice == "Wskaźnik rentowności netto sprzedaży":
            st.write("""
                    Wskaźnik ten utrzymywał się na bardziej
                    stabilnym poziomie niż dwa poprzednie wskaźniki. Spadek tego wskaźnika
                    pomiędzy 2020 a 2021 rokiem świadczy o gorszej sytuacji finansowej spółki w 2021
                    roku. Mimo wszystko wskaźnik ten utrzymuje się na wysokim poziomie w 2021 roku. 
            """)
        #Dane do wykresu
        data = {
            "Nazwa wskaźnika": [
                "Wskaźnik rentowności netto kapitału własnego (B*C)", 
                "Wskaźnik rentowności netto aktywów(D*E)", 
                "Mnożnik kapitału własnego", 
                "Wskaźnik rentowności netto sprzedaży", 
                "Wskaźnik rotacji aktywów"
            ],
            "2019": [15.86, 12.49, 1.2699, 33.63, 0.3712],
            "2020": [52.77, 39.88, 1.3233, 53.97, 0.7390],
            "2021": [11.03, 9.68, 1.1396, 23.52, 0.4114]
        }
        df = pd.DataFrame(data)
        #Wygląd wykresu
        df_long = pd.melt(df, id_vars=["Nazwa wskaźnika"], var_name="Rok", value_name="Wartość")
        fig = px.bar(df_long, x="Nazwa wskaźnika", y="Wartość", color="Rok", barmode="group",
                    title="Analiza Wskaźników Finansowych CD Projekt w latach 2019-2021",
                    labels={"Nazwa wskaźnika": "Wskaźniki Finansowe", "Wartość": "Wartość (%)", "Rok": "Rok"})
        st.plotly_chart(fig)

if mode == 'Analiza strategii 🧭':

    st.title("Analiza strategii 🧭")

    tab1, tab2, tab3 = st.tabs(["5 sił Portera 💼", "Analiza SWOT 💼", "Analiza strategii 💼"])

    with tab1:

        options = ["Największy wpływ", "Średni wpływ", "Najmniejszy wpływ"] 
        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Największy wpływ":
            st.write(""" 
                    Konkurencją dla firmy CD
                    Projekt na rynku światowym są inne firmy zajmujące się produkcją wysokobudżetowych gier.
                    Wśród elementów, które miały największy wpływ na rywalizację należy
                    wymienić przewagę jakościową oraz 
                    konkurencja cenowa.
                    """)
            
        if choice == "Średni wpływ":
            st.write(""" 
                        Na drugim miejscu wśród rozpatrywanych kategorii znajduje się groźba nowych wejść na
                        dany rynek. Suma ocen ważonych tej pozycji wynosi aż 4,1. W skład rynku gier pragnie wejść
                        coraz więcej nowych firm, jednak jest to ograniczone dużymi barierami wejścia. 
                    """)
                
        if choice == "Najmniejszy wpływ":
            st.write(""" 
                        Na kolejnym miejscu z kolei można zaobserwować siłę oddziaływania nabywców.
                        Elementem, który posiada największą wartość w tej kategorii jest ocena jakości przez klienta.
                        Od tej oceny zależy właśnie sprzedaż produktu przez spółkę CD Projekt. Ocena ta jest istotna,
                        gdyż jest mnóstwo stron internetowych, które piszą recenzje danych gier. Ponadto klienci mogą
                        wystawiać oceny danym grą. Wartość zagrożenia od strony substytutówi siła
                        oddziaływania dostawców nie stanowi dużego zagrożenia.
                    """)
        #Dane do wykresu
        data = {
            "Czynnik": [
                "Dynamika wzrostu sektora", "Konkurencja cenowa", "Poziom przewagi technologicznej", 
                "Kadra pracownicza", "Przewaga jakościowa", "Reputacja marki",
                "Bariery wejścia", "Poziom technologii", "Renoma marek", "Strategie promocyjne", "Stopień zróżnicowania produktów",
                "Dostępność substytutów", "Przewaga konkurencji cenowej", "Poziom jakości substytutu",
                "Znaczenie branży dla dostawcy", "Jakość dostawcy", "Ryzyko zmiany dostawcy",
                "Wielkość zakupu przez nabywców", "Ocena jakości przez klienta", "Występowanie substytutów"
            ],
            "Waga": [
                0.10, 0.10, 0.15, 0.15, 0.30, 0.20,
                0.30, 0.20, 0.30, 0.15, 0.05,
                0.20, 0.40, 0.40,
                0.30, 0.60, 0.10,
                0.30, 0.40, 0.30
            ],
            "Siła wpływu": [
                3, 4, 4, 3, 5, 5,
                5, 4, 4, 3, 3,
                2, 2, 2,
                2, 2, 1,
                3, 3, 2
            ],
            "Ocena ważona": [
                0.3, 0.4, 0.6, 0.45, 1.5, 1.0,
                1.5, 0.8, 1.2, 0.45, 0.15,
                0.4, 0.8, 0.8,
                0.6, 1.2, 0.1,
                0.9, 1.2, 0.6
            ]
        }

        df = pd.DataFrame(data)
        #Wykres
        df_long = pd.melt(df, id_vars=["Czynnik"], value_vars=["Waga", "Siła wpływu", "Ocena ważona"],
                        var_name="Rodzaj", value_name="Wartość")
        fig = px.line_polar(df_long, r="Wartość", theta="Czynnik", color="Rodzaj", line_close=True,
                            title="Ocena ważona czynników siły konkurencyjnej")
        st.plotly_chart(fig)

    with tab2:

        options = ["Mocne strony", "Słabe strony", "Szanse", "Zagrożenia"] 
        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Mocne strony":
            st.write("""
        - Znana i ceniona seria gier Wiedźmin
        - Wykwalifikowana kadra pracownicza
        - Dobra struktura finansowania
        - Własna platforma sprzedażowa
        """)
            
        if choice == "Słabe strony":
            st.write(""" 
        - Duża rotacja pracowników
        - Nieudana premiera gry Cyberpunk 2077
        - Mało marek gier
        """)
            
        if choice == "Szanse":
            st.write("""
        - Coraz większa popularność gier komputerowych
        - Wzrost wartości rynku gier
        """)
            
        if choice == "Zagrożenia":
            st.write("""
        - Rosnąca konkurencja
        - Piractwo gier
        - Wahania cen walut
        """)
        #Dane do SWOT
        categories = ["Mocne strony", "Słabe strony", "Szanse", "Zagrożenia"]
        weights = [4, 3, 2, 4]
        #Wygląd wykresu
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=categories, 
            y=weights,
            marker_color=['green', 'red', 'blue', 'orange']
        ))
        fig.update_layout(
            title="Wagi kategorii SWOT CD Projekt",
            xaxis=dict(title="Kategoria"),
            yaxis=dict(title="Waga"),
            showlegend=False,
            font=dict(size=14)
        )
        st.plotly_chart(fig)

    with tab3:

        options = ["Strategia produkcyjna", "Strategia finansowa", "Strategia marketingowa", "Strategia rozwojowa", "Strategia zasobów ludzkich"] 
        choice = st.select_slider("Wybierz pozycję do analizy:", options=options)

        if choice == "Strategia produkcyjna":
            st.write("""
                    - Spółka stara się być niezależna finansowo,
                    - CD Projekt jest spółką rejestrowaną na Giełdzie Papierów Wartościowych, w związku
                    z tym spółka jest w stanie zdobyć środki finansowe poprzez wyemitowane akcje,
                    - Spółka posiada bardzo dobrą strukturę elementów bilansu. Co więcej, spółka posiada
                    bardzo wysokie wkłady własne w spółkę,
                    - Sprawozdania finansowe dla spółki w latach 2019-2021 prezentują się nadzwyczaj
                    korzystnie,
                    - Spółka posiada bardzo dobrą relację wartości pasywów do aktywów,
                    - Spółka stara się utrzymywać wskaźniki rentowności na wysokim poziomie,
                    - Spółka utrzymuje przepływy pieniężne z działalności operacyjnej w wartościach
                    dodatnich, dzięki czemu jest w stanie finansować działalność środkami pozyskanymi z
                    działalności operacyjnej.""")

        if choice == "Strategia finansowa":
            st.write("""
            - CD Projekt tworzy rozbudowane gry fabularne z otwartym światem. Wyprodukowanie
            takich gier jest bardzo czasochłonne oraz kosztowne. CD Projekt stara się, aby każdy z
            produktów cechował się jak najlepszą jakością, a gry testowane są przez testerów,
            - Główne biuro CD PROJEKT zlokalizowane jest w Warszawie,
            - W tworzeniu gier spółka używa specjalistycznego sprzętu elektronicznego,
            oprogramowania oraz technologii,
            - CD Projekt używa również „RED Engine”, który umożliwia tworzenie bardziej
            rozbudowanych gier,
            - Firma stale poprawia wydajność gier, usuwa napotkane błędy oraz aktualizuje swoje
            produkty.""")

        if choice == "Strategia marketingowa":
            st.write("""
            - Spółka produkuje gry na skalę światową,
            - Grupą docelową przedsiębiorstwa są gracze,
            - Spółka zarządza własną stronę internetową oraz sklepem promującym gry GOG.com,
            - Spółka promuje swoje produkty poprzez rozbudowaną sieć kontaktów,
            - Przed wypuszczeniem na rynek gry wyprodukowane przez firmę są testowane,""")

        if choice == "Strategia rozwojowa":
            st.write("""
            - Spółka koncentruje się na kluczowych produktach, do których możemy zaliczyć grę
            „Wiedźmin”, a także „Cyberpunk 2077”. CD Projekt stara się również na bieżąco
            wprowadzać innowacje,
            - Spółka CD Projekt buduje również zespoły z szerokimi kompetencjami. Dzięki
            stworzeniu takich zespołów łatwiej jest znaleźć innowacyjne rozwiązania. Co więcej,
            praca jest efektywniejsza,
            - Przedsiębiorstwo inwestuje w nowy sprzęt elektroniczny, oprogramowania oraz
            technologie,
            - Firma stale zwiększa liczebność zespołu,
            - CD PROJEKT planuje utworzyć nowe placówki w kluczowych dla firmy lokalizacjach.""")

        if choice == "Strategia zasobów ludzkich":
            st.write("""
            - W CD Projekt pracuje ponad 750 wysoko wykwalifikowanych pracowników,
            - Firmę prowadzą ludzie, którzy mają doświadczenie w branży gier,
            - Spółka zamierza również rozbudowywać oraz wspierać sklep internetowy GOG.com.""")

if mode == 'Podsumowanie 💎':

    st.title("Podsumowanie 💎")

    tab1, tab2, tab3 = st.tabs(["Podsumowanie ✨", "Wnioski 🕵️‍♂️", "Źródła 📂"])

    with tab1:
        st.write("""
        - Wzrost aktywów ogółem o 34,96%.
        - Dominacja aktywów obrotowych w strukturze bilansu.
        - Wysoki udział kapitału własnego, co oznacza solidne finansowanie.
        - Zysk netto wzrósł o 16,08%.
        - Przepływy pieniężne z działalności operacyjnej dodatnie.
                 """)

    with tab2:
        st.write("""
        CD Projekt stara się utrzymać swoją pozycję na rynku poprzez:
        - Projektowanie nowych gier.
        - Rozbudowę zespołów i placówek.
        - Promowanie gier i utrzymywanie kontaktów z graczami oraz partnerami.
        - Inwestycje w nowe technologie i sprzęt.
        - Wdrażanie innowacji i usprawnień.
        Regularna analiza finansowa i strategiczna jest kluczowa dla utrzymania przewagi konkurencyjnej i stabilnego wzrostu.
                 """)
        
    with tab3:
        st.write("""Moja praca magisterska oraz bibliografia znajdują się w załączniku poniżej
""")
        # Ścieżka do pliku PDF
        file_path = "company/pracamagisterska.pdf"

        # Tworzenie przycisku do pobrania pliku
        with open(file_path, "rb") as file:
            st.download_button(
                label="Pobierz Pracę Magisterską",
                data=file,
                file_name="company/pracamagisterska.pdf",
                mime="application/pdf"
            )

        

           





















             


