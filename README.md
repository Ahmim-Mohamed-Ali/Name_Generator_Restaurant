# Restaurant Name Generator

Une application Streamlit pour générer des noms de restaurants et des menus en fonction de la cuisine choisie grace a OpenAi et son API.

## Prérequis

- Python 3.7 ou supérieur
- Clé API OpenAI

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre_nom_utilisateur/votre_depot.git

2. Naviguez dans le Dépot:
  cd votre_depot

3. Installez Les Dépendances:

  pip install -r requirements.txt

4. Obtenez Une Clé API:

Obtenez une clé API OpenAI en vous inscrivant sur OpenAI.

5. Créez un fichier secret_key.py dans le répertoire principal et ajoutez votre clé API:

import os

os.environ['OPENAI_API_KEY'] = 'sk-........'

- 6. Exécutez l'application Streamlit :
   streamlit run main.py
   
# Utilisation
Sélectionnez une cuisine dans le menu latéral pour générer un nom de restaurant et ses plats.
