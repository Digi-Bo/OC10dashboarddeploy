
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go



##
## Ceci est une app de recommandation de contenu qui appelle une fonction Azure


# Titre de l'application
st.title("Dasboard Projet 10 : Comparatif des modèles pour un système de recommandation")

# Charger les données
df_results = pd.read_csv('ResultatsOC10.csv')



#### DASHBOARD

if st.button("Découvrir le dashboard"):
    st.session_state.dashboard_view = True
else:
    st.session_state.dashboard_view = False


###  Si le tableau de bord est actif (st.session_state.dashboard_view == True).
if st.session_state.dashboard_view:

    # Filtrer le dataframe pour la "strategie 2"
    df_strategie2 = df_results[df_results['Stratégie'] == "Stratégie 1"]

    # Filtrer le dataframe filtré en fonction du type d'algorithme
    df_implemente = df_strategie2[df_strategie2["Type d'algorithme"] == "implémenté"]
    df_default = df_strategie2[df_strategie2["Type d'algorithme"] == "Par défaut"]

    # Tri des dataframes par 'test_rmse' pour un affichage plus esthétique
    df_implemente = df_implemente.sort_values(by='test_rmse', ascending=False)
    df_default = df_default.sort_values(by='test_rmse', ascending=False)

    # Créer le graphique
    fig = go.Figure()

    # Ajouter les barres pour les algorithmes "implémenté"
    fig.add_trace(go.Bar(
        x=df_implemente['Algorithm'],
        y=df_implemente['test_rmse'],
        name='Implémenté',
        marker_color='indianred'
    ))

    # Ajouter les barres pour les algorithmes "Par défaut"
    fig.add_trace(go.Bar(
        x=df_default['Algorithm'],
        y=df_default['test_rmse'],
        name='Par défaut',
        marker_color='lightsalmon'
    ))

    # Mettre à jour le layout
    fig.update_layout(
        title="Comparaison des RMSE des algorithmes pour la stratégie 1",
        xaxis_title="Algorithmes",
        yaxis_title="Test RMSE",
        barmode='group'
    )

    st.plotly_chart(fig)


    # Filtrer le dataframe pour la "Stratégie 1"
    df_strategie1 = df_results[df_results['Stratégie'] == "Stratégie 1"]

    # Filtrer le dataframe filtré en fonction du type d'algorithme
    df_implemente = df_strategie1[df_strategie1["Type d'algorithme"] == "implémenté"]
    df_default = df_strategie1[df_strategie1["Type d'algorithme"] == "Par défaut"]

    # Tri des dataframes par 'fit_time' pour un affichage plus esthétique
    df_implemente = df_implemente.sort_values(by='fit_time', ascending=False)
    df_default = df_default.sort_values(by='fit_time', ascending=False)

    # Créer le graphique
    fig = go.Figure()

    # Ajouter les barres pour les algorithmes "implémenté"
    fig.add_trace(go.Bar(
        x=df_implemente['Algorithm'],
        y=df_implemente['fit_time'],
        name='Implémenté',
        marker_color='indianred'
    ))

    # Ajouter les barres pour les algorithmes "Par défaut"
    fig.add_trace(go.Bar(
        x=df_default['Algorithm'],
        y=df_default['fit_time'],
        name='Par défaut',
        marker_color='lightsalmon'
    ))

    # Mettre à jour le layout
    fig.update_layout(
        title="Comparaison des temps d'entraînement (fit_time) pour la Stratégie 1",
        xaxis_title="Algorithmes",
        yaxis_title="Temps d'entraînement (fit_time)",
        barmode='group'
    )

    st.plotly_chart(fig)