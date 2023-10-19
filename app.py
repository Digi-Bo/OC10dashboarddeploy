
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from azure.storage.blob import BlobServiceClient
import os

## Fonction pour accéder au blob storage

def load_data_from_blob_storage(container_name, blob_name, file_type):
    """
    Charge les données à partir du stockage Blob.

    Args:
        container_name (str): Nom du conteneur Blob.
        blob_name (str): Nom du blob.
        file_type (str): Type de fichier (csv ou pickle).

    Returns:
        pd.DataFrame or object: Les données chargées depuis le stockage Blob.
    """ 
        
    # Récupérer la chaîne de connexion au stockage Azure à partir des variables d'environnement
    connection_string = os.environ["AzureWebJobsStorage"]

    # Créer un client BlobService à partir de la chaîne de connexion
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Obtenir le client du conteneur spécifié
    container_client = blob_service_client.get_container_client(container_name)

    # Obtenir le client du blob spécifié
    blob_client = container_client.get_blob_client(blob_name)

    # Télécharger le contenu du blob
    data = blob_client.download_blob()
    
    if file_type == 'csv':
        # Si le type de fichier est CSV, charger les données en tant que DataFrame pandas à partir des données CSV
        return pd.read_csv(io.BytesIO(data.readall()))
    elif file_type == 'pickle':
        # Si le type de fichier est pickle, charger les données en tant qu'objet à partir des données pickle
        return pickle.loads(data.readall())
    else:
        # Si le type de fichier n'est pas pris en charge, lever une exception ValueError
        raise ValueError("Unsupported file_type")




# Titre de l'application
st.title("Dasboard Projet 10 : Comparatif des modèles pour un système de recommandation")

# Charger les données depuis le blob storage
df_results = load_data_from_blob_storage(container_name="mycontainer", blob_name="ResultatsOC10.csv", file_type="csv")



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


        # Filtrer le dataframe pour la "Stratégie 1"
    df_strategie1 = df_results[df_results['Stratégie'] == "Stratégie 1"]

    # Filtrer le dataframe filtré en fonction du type d'algorithme
    df_implemente = df_strategie1[df_strategie1["Type d'algorithme"] == "implémenté"]
    df_default = df_strategie1[df_strategie1["Type d'algorithme"] == "Par défaut"]

    # Tri des dataframes par 'test_time' pour un affichage plus esthétique
    df_implemente = df_implemente.sort_values(by='test_time', ascending=False)
    df_default = df_default.sort_values(by='test_time', ascending=False)

    # Créer le graphique
    fig = go.Figure()

    # Ajouter les barres pour les algorithmes "implémenté"
    fig.add_trace(go.Bar(
        x=df_implemente['Algorithm'],
        y=df_implemente['test_time'],
        name='Implémenté',
        marker_color='indianred'
    ))

    # Ajouter les barres pour les algorithmes "Par défaut"
    fig.add_trace(go.Bar(
        x=df_default['Algorithm'],
        y=df_default['test_time'],
        name='Par défaut',
        marker_color='lightsalmon'
    ))

    # Mettre à jour le layout
    fig.update_layout(
        title="Comparaison des temps de test (test_time) pour la Stratégie 1",
        xaxis_title="Algorithmes",
        yaxis_title="Temps de test (test_time)",
        barmode='group'
    )

    st.plotly_chart(fig)
