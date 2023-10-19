
import streamlit as st
import pandas as pd

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

