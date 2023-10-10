# OC09-streamit-contentreco-deploy

## Créer les bons secrêts sur github pour le déploiement

Voici les étapes pour créer un secret avec le profil de publication de votre application Web:

1. Connectez-vous au [portail Azure](https://portal.azure.com/).
2. Accédez à votre application Web (Web App) que vous avez créée précédemment.
3. Dans le menu de gauche, recherchez la section "Settings" (Paramètres) et cliquez sur "Deployment Center" (Centre de déploiement).
4. Dans le Centre de déploiement, choisissez, au niveau de **source** , il faut choisir "GitHub action" comme source de code, puis cliquez sur "Get Publish Profile" (Gérer le profil de publication) en haut de la page. Un fichier XML sera téléchargé sur votre ordinateur.
5. Ouvrez le fichier XML téléchargé avec un éditeur de texte (comme Notepad ou Visual Studio Code) et copiez son contenu.
6. Allez dans votre dépôt GitHub, cliquez sur l'onglet "Settings" (Paramètres), puis sur "Secrets" dans le menu de gauche.
7. Cliquez sur "New repository secret" (Nouveau secret de dépôt) en haut à droite.
8. Entrez un nom pour le secret, par exemple `WEB_APP_PUBLISH_PROFILE`, et collez le contenu du fichier XML dans la zone "Value" (Valeur). Cliquez sur "Add secret" (Ajouter un secret).
