# SeraHub

SeraHub est une plateforme de type réseau social conçue avec Django Rest Framework (DRF), qui permet aux utilisateurs de publier des annonces, de les commenter, et de gérer leurs profils personnels.

## Fonctionnalités principales

- **Gestion des utilisateurs** :
  - Inscription avec validation par e-mail.
  - Connexion sécurisée via un jeton d'authentification (JWT).
  - Réinitialisation du mot de passe.

- **Publications d'annonces** :
  - Création, mise à jour, suppression, et lecture des annonces.
  - Possibilité d'ajouter plusieurs images aux annonces.

- **Commentaires** :
  - Commentaires sur les annonces d'autres utilisateurs.
  - Les commentaires liés à une annonce sont supprimés lorsque l'annonce est supprimée.

- **Interface API** :
  - Basée sur Django Rest Framework, accessible via `/api/`.

## Structure du projet

```
SeraHub/
├── .venv/              # Environnement virtuel Python
├── api/                # Application principale pour la gestion des APIs
├── comments/           # Gestion des commentaires
├── media/              # Dossier pour les fichiers téléversés (images des annonces)
├── posts/              # Gestion des annonces
├── SeraHub/            # Configuration du projet Django
├── users/              # Gestion des utilisateurs et de leurs profils
├── manage.py           # Fichier principal pour les commandes Django
├── requirements.txt    # Dépendances Python du projet
```

## Installation

### Prérequis

- Python 3.9 ou supérieur
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Étapes

1. Clonez le dépôt :

   ```bash
   git clone <URL_DU_DÉPÔT>
   cd SeraHub
   ```

2. Créez et activez un environnement virtuel :

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Sous Windows
   source .venv/bin/activate # Sous macOS/Linux
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations de base de données :

   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur local :

   ```bash
   python manage.py runserver
   ```

6. Accédez à l'API via : `http://127.0.0.1:8000/api/`.

## Exemple de requête API

### Inscription d'un utilisateur

#### Requête

```json
POST /api/users/
{
  "username": "testuser",
  "first_name": "test",
  "last_name": "user",
  "email": "testuser@example.com",
  "password": "securepassword123"
}
```

#### Réponse

```json
{
  "message": "Un email de confirmation a été envoyé à votre adresse."
}
```

## Développement

- **Framework principal** : Django
- **API REST** : Django Rest Framework
- **Base de données** : PostgreSQL
- **Authentification** : JSON Web Token (JWT)

## Contributeurs

- **Nom** : Kerenah
- **Contact** : kerenahramantoanina@gmail.com
