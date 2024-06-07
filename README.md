# DownloadGradesFromParis1EPI
les étudiants de l'Université Paris 1 Panthéon-Sorbonne à partir du système EPI (Espace Pédagogique Interactif). Le script utilise Selenium pour naviguer et interagir avec le portail web de l'université, en simulant des actions utilisateur pour accéder et télécharger les documents nécessaires.

# Fonctionnalités principales:
Connexion Automatisée: Le script se connecte automatiquement au portail EPI de l'Université Paris 1 en utilisant les identifiants fournis.
Navigation et Téléchargement: Après la connexion, il navigue jusqu'à la section des notes et résultats, sélectionne la filière spécifique de l'utilisateur, et télécharge le bulletin de notes correspondant.
Envoi d'Emails: Une fois le téléchargement effectué, le script peut également envoyer le document téléchargé par e-mail à une adresse spécifiée, facilitant ainsi l'accès aux documents importants sans nécessiter une interaction manuelle constante.

# IdParis1 : votre identifiant de connexion à l'EPI/ENT de l'université Paris 1 Panthéon Sorbonne
# PasswordParis1 : votre mot de passe pour vous connecter à l'EPI/ENT de Paris 1
# Filière_inscription : l'intitulé exact de votre formation comme affiché Exams>Notes & Résultats > copier/ coller le nom exact de la formation pour laquelle vous voulez le bulletin de notes
# To : l'adresse mail à qui il faut envoyer le document 
# fromMail : l'adresse gmail à partir de laquelle le mail est envoyé
# fromPassword : le mot de passe application de l'adresse gmail à partir de laquelle le mail est envoyé
