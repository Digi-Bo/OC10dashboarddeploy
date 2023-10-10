
import streamlit as st
import requests  
import os



##
## Ceci est une app de recommandation de contenu qui appelle une fonction Azure


# Titre de l'application
st.title("Système de recommandation basé sur le contenu")

# Sélection de l'utilisateur
user_id = st.number_input("Entrez l'ID de l'utilisateur :", min_value=1, max_value=1000, value=1)

# Bouton pour lancer la recommandation
if st.button("Recommander des articles"):
    
    # Récupération du token dans les secrêt
    azure_function_token = os.environ.get("AZURE_FUNCTION_TOKEN")

    # URL en ajoutant le token
    azure_function_url = f"https://hybridrecommender.azurewebsites.net/api/content4-last-click-acp?code={azure_function_token}"

    try:
        # Envoyer une requête GET à la fonction Azure
        response = requests.get(
            azure_function_url,
            params={
                "userid": user_id
            },
        )

        # Vérifier le statut de la réponse
        response.raise_for_status()

        # Tenter de lire la réponse comme JSON
        top_articles = response.json()

        # Afficher les résultats
        st.header("Top articles recommandés :")
        for article in top_articles:
            st.write(f"ID de l'article : {article}")

    except requests.exceptions.HTTPError as http_err:
        st.error(f"Erreur HTTP s'est produite: {http_err}")
    except Exception as err:
        st.error(f"Une erreur s'est produite: {err}")
