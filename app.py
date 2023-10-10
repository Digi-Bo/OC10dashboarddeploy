import streamlit as st
import pandas as pd
from datetime import datetime, time
import requests  

##
## App proposant la connexion à une fonction azure de recommendation de contenu basé sur le contenu
## 


# Titre de l'application
st.title("Système de recommandation basé sur le contenu")

# Sélection de l'utilisateur
user_id = st.number_input("Entrez l'ID de l'utilisateur :", min_value=1, max_value=1000, value=1)

# Dates pour la période de prédiction
pred_start_date = st.date_input("Date de début de la période de prédiction :", value=pd.to_datetime('2017-10-09'))
pred_end_date = st.date_input("Date de fin de la période de prédiction :", value=pd.to_datetime('2017-10-16'))

# Convertir les objets date en objets datetime avec une heure de 0
pred_start_date = datetime.combine(pred_start_date, time(0, 0))
pred_end_date = datetime.combine(pred_end_date, time(0, 0))

# Bouton pour lancer la recommandation
if st.button("Recommander des articles"):
    if pred_end_date < pred_start_date:
        st.error("La date de fin doit être ultérieure à la date de début.")
    else:
        # Adresse de la fonction Azure basée sur le contenu
        azure_function_url = "https://hybridrecommender.azurewebsites.net/api/content4-last-click-acp?code=NDrrUwHnsMHb8gBEI4GmIibW8OWlYrPtBa8HoDKSUPr1AzFuGqhWSw=="
                                
        try:
            # Envoyer une requête GET à la fonction Azure
            response = requests.get(
                azure_function_url,
                params={
                    "userid": user_id,
                    "pred_start_date": pred_start_date.strftime('%Y-%m-%d'),
                    "pred_end_date": pred_end_date.strftime('%Y-%m-%d'),
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
