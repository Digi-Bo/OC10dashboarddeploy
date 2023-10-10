
import streamlit as st
import requests  

# Titre de l'application
st.title("Système de recommandation basé sur le contenu")

# Sélection de l'utilisateur
user_id = st.number_input("Entrez l'ID de l'utilisateur :", min_value=1, max_value=1000, value=1)

# Bouton pour lancer la recommandation
if st.button("Recommander des articles"):
    # Adresse de la fonction Azure basée sur le contenu
    azure_function_url = "https://hybridrecommender.azurewebsites.net/api/content4-last-click-acp?code=Nz3pKOLCAk8mUhxJEbOFTyd33asChi2jiyg2u9i4TA-OAzFuWHXtBg=="
    
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
