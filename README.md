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

## Django

### Détail des pages
- Page admin
    - [X] Importer projet
        - Création des utilisateurs
        - Création ds formulaires
- Accès formateur -> Base user django | Accès via `login_required()`
    - [X] Affichage des TOUS les formulaires (liste) : Status, date, lien étudiant, lien modification
    - [X] Details des formulaires : statistiques et réponses individuelles
- Accès étudiant -> Base user perso. | Accès via token JWT
    - [X] Page de login (formulaire) : Génération du token JWT
        - [ ] Page de login : gérer les sessions déjà connectées
    - [X] Bouton logout : Suppression du token
    - [ ] Affichage des formulaires ouverts
    - [X] Page de réponse au formulaire : 
    -> [X] Si réponse déjà présente, pré-remplir le formulaire
    -> [ ] Fonction collecte de réponses

### Fichier **env**
***Fichier non git*** (faire de même pour les identifiants dans *settings.py*)
```
SECRETS = {
    'JWT' : *type:string*,         
    'JWT_algo' : *type:string*,    
    'SALT' : *type:byte*            
}
```

## Flask

- [ ] API collecte des réponses et update entées BDD 
- [ ] CORS

## MISC
- [ ] Commenter tout le code 
- [ ] Ajouter du style CSS
- [ ] Header + Footer ?
- [ ] Gestion des erreurs plus poussée
- [ ] Optimisation