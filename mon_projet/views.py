from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from collections import defaultdict
import jwt
from .models import Etudiant
from .models import Formulaire
from .models import ReponsesFormulaire
from .forms import LoginForm
from . import utility, env

# Page 'home' : Lien vers la page admin, la page formateur et la page étudiant
def home(request):
    return HttpResponse(("<a href='/admin/'>Panel Admin</a><br/><a href='/formateur/'>Page formateur</a><br/><a href='/etudiant/'>Page étudiant</a>"))

# Décorateur fourni par django pour protéger les pages par une authentification à la base d'utilisateur par défaut
@login_required(login_url="/admin/login/?next=/formateur/")
# Fonctiopn d'affichage de base formateur
def formateur_list(request):
    # On inclut tous les formulaires
    formulaires = Formulaire.objects.all()
    return render(request, 'formateur_list.html', {'formulaires': formulaires})

# Décorateur fourni par django pour protéger les pages par une authentification à la base d'utilisateur par défaut
@login_required(login_url="/admin/login/?next=/formateur/<str:id_formulaire>/")
# Fonction d'affichage détaillé d'un formulaire
def formateur_details(request, id_formulaire):
    # Récupérer toutes les entrées de la table ReponsesFormulaire en fonction de l'id du formulaire
    reponses = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire)
    # Variables : total de réponses, moyenne de progression
    total_reponses = reponses.count()
    moy_progression = reponses.aggregate(avg_progression=Avg('progression'))['avg_progression'] or 0
    # Initialisation des dictionnaires de difficulté et de maitrise
    count_difficulte = defaultdict(int)
    count_maitrise = defaultdict(int)
    
    # Incrémentation du count des difficultés
    for reponse in reponses:
        if reponse.difficulte:
            count_difficulte[reponse.difficulte] += 1
        if reponse.maitrise:
            count_maitrise[reponse.maitrise] += 1

    return render(request, 'formateur_details.html', {
        'id_formulaire' : id_formulaire,
        'reponses': reponses,
        'total_reponses': total_reponses,
        'moy_progression': moy_progression,
        'count_difficulte' : count_difficulte.items(),
        'count_maitrise' : count_maitrise.items()
    })

# Page de login pour les étudiants
def etudiant_login(request):
    # Si absence du cookie 'JWT'
    if not request.COOKIES.get('JWT'):
        # Importer le formulaire
        form = LoginForm()
        message = ''
        # N'accepter que les requêtes en POST
        if request.method == 'POST':  
            # Récuperer le contenu du formulaire retourné 
            form = LoginForm(request.POST)   
            # Validation du formulaire 
            if form.is_valid():
                # Récupération des variables username et password (avec hash du mot de passe pour plus tard)
                username = form.cleaned_data['username']
                password = utility.hash_password(form.cleaned_data['password'])

                # Vérification de correspondance username et password avec la base de donnée 
                try:
                    Etudiant.objects.get(username=username, password=password)
                    # Si étudiant existant, générer un token JWT avec son username
                    token = utility.generate_jwt(username)
                    # Rediriger l'utilisateur et ajouter le cookie au navigateur
                    reponse = HttpResponseRedirect('/etudiant/')
                    reponse.set_cookie('JWT', token)
                    return reponse
                # Si utilisateur inexistant, message d'erreur
                except Etudiant.DoesNotExist:
                    message = 'Utilisateur ou mot de passe incorrect !'

        return render(request, 'etudiant_login.html', {
            'form' : form, 
            'message' : message })
    # Si cookie 'JWT' déjà présent, alors utilisateur déjà connecté. Proposer une redirection vers la page étudiant ou logout
    else:
        return HttpResponse("Déjà connecté<br/><a href='/etudiant/'>Formulaires</a><br/><a href='/logout/'>Logout</a>")

# Fonction de logout
def etudiant_logout(request):
    try:
        # Supprimer le cookie et rediriger vers login
        reponse = redirect('/login/')
        reponse.delete_cookie('JWT')
        return reponse
    except:
        return HttpResponse("Une erreur s'est produite")
    
# Fonction affichage de base étudiant
def etudiant_list(request):
    # Vérification de la connexion utilisateur via son token
    try:
        # Récupérer le token -> payload -> username
        token = request.COOKIES.get('JWT')
        payload = utility.decode_jwt(token)
        username = payload['username']
        # Si on arrive a récupérer le username, alors afficher tous les formulaire ayant le status ouvert
        if username:
            formulaires = Formulaire.objects.filter(ouvert=True)
            return render(request, 'etudiant_list.html', {'formulaires': formulaires})
        # Sinon, renvoyer a la page d'accueil
        else:
            return HttpResponseRedirect('/login/')
    # Gestion des erreurs : Expiration, Invalid, Username
    except jwt.ExpiredSignatureError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse
    except jwt.InvalidTokenError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse
    except KeyError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse

# Fonction d'affichage de formulaire en fonction de son id
def etudiant_formulaire(request, id_formulaire):
    # Vérification de la connexion utilisateur via son token
    try:
        # Récupérer le token -> payload -> username
        token = request.COOKIES.get('JWT')
        payload = utility.decode_jwt(token)
        username = payload['username']
        # Si on arrive a récupérer le username :
        if username:
            # Récupérer les information du formulaire (id_formulaire)
            formulaire = Formulaire.objects.filter(id_formulaire=id_formulaire).first()
            # Vérification de son status, il doit être ouvert
            if formulaire.ouvert:
                # Si ouvert -> Récupérer la réponse de l'utilisateur avec sa liaison numero_etudiant (foreign key) et son username
                reponse = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire, numero_etudiant__username__iexact=username).first()
                # Si pas de réponse de l'utilisateur
                if not reponse:
                    # Récupérer ses informations
                    etudiant = Etudiant.objects.filter(username=username).first()
                    # Initialiser une première 'réponse' : id_formulaire, numero_etudiant et la date d'accès
                    init = ReponsesFormulaire.objects.create(id_formulaire_id=id_formulaire, numero_etudiant_id=etudiant.numero_etudiant, date_access=timezone.now())
                    init.save()
                    # Récupérer la 'nouvelle' réponse de l'utilisateur que l'on vient d'initialiser
                    reponse = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire, numero_etudiant__username__iexact=username).first()
                # Variable de l'API Flask
                urlAPI = env.API_FLASK
                return render(request, 'etudiant_formulaires.html', {
                    'formulaire' : formulaire,
                    'reponse' : reponse,
                    'urlAPI' : urlAPI})
            # Si formulaire fermé, notifier l'utilisateur + bouton retour
            else:
                return HttpResponse("Formulaire <span style='color: rgb(224, 42, 42);''>fermé</span>. <br/><a href='/etudiant/'>Retour</a>")
        else:
            return HttpResponseRedirect('/login/')
    # Gestion des erreurs : Expiration, Invalid, Username
    except jwt.ExpiredSignatureError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse
    except jwt.InvalidTokenError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse
    except KeyError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse