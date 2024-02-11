# Projet Python 2 - Livecampus 

## BDD
Réalisée via Django

### Etudiant
- numero_etudiant -> int, primary key (auto increment & not null)
- username -> varchar, unique, not null
- nom -> varchar, not null
- prenom -> varchar, not null
- password -> varchar, not null
- email -> varchar (email), unique, not null
-> Pour le mot de passe, fonction `save()` bcrypt

### Formulaire
- id_formulaire -> int, primary key (auto increment & not null)
- ouvert -> bool, default=True
- date_ouverture -> datetime, default=now
- date_fermeture -> datetime
- nom formulaire -> varchar, not null
-> Pour les dates, fonction `save()`avec conditions

### ReponsesFormulaire
- id -> Auto (Primary key)
- id_formulaire -> Foreign key Formulaire
- numero_etudiant -> Foreign key Etudiant
- progression -> int, not null
- difficulte -> varchar, not null
- maitrise -> varchar, not null

## Django ![](https://geps.dev/progress/95)

### Détail des pages
- Page admin
    - [X] Importer projet (INSTALLED_APPS)
        - Création des utilisateurs
            - [ ] Page création etudiant perso
        - Création ds formulaires
            - [ ] Page création formulaire perso
- Accès formateur -> Base user django | Accès via `login_required()`
    - [X] Affichage des TOUS les formulaires (liste) : Status, date, lien étudiant, lien modification
    - [X] Details des formulaires : statistiques et réponses individuelles
- Accès étudiant -> Base user perso. | Accès via token JWT
    - [X] Page de login (formulaire) : Génération du token JWT
        - [X] Gérer les sessions déjà connectées
    - [X] Bouton logout : Suppression du token
    - [X] Affichage des formulaires avec status ouvert (liste)
    - [X] Page de réponse au formulaire : 
        - [X] Si réponse déjà présente, pré-remplir le formulaire
        - [X] Date premier accès
        - [X] Fonction collecte de réponses -> [Flask](#flask)

### Fichier **env**
***Fichier non git*** (Note : faire de même pour les identifiants dans *settings.py*)
```
SECRETS = {
    'JWT' : <type:string>,         
    'JWT_algo' : <type:string>,    
    'SALT' : <type:byte>            
}

API_FLASK = 'http://127.0.0.1:5000'
```

### Utilisateurs de test
- **Formateur** : `admin:Pa$$w0rd`
- **Etudiant** : `etudiant1:Pa$$w0rd`

## Flask ![](https://geps.dev/progress/85)

- [X] CORS
- [X] API collecte des réponses 
- [X] Update entées BDD 
- [ ] Gestion des sessions (token)

## MISC ![](https://geps.dev/progress/50)
- [X] Commenter tout le code 
- [ ] Ajouter du style CSS
- [ ] Header + Footer ?
- [X] Gestion des erreurs
    - [ ] OPlus poussé 
- [ ] Optimisation