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

def home(request):
    return HttpResponse(("<a href='/admin/'>Panel Admin</a><br/><a href='/formateur/'>Page formateur</a><br/><a href='/etudiant/'>Page étudiant</a>"))

@login_required(login_url="/admin/login/?next=/formateur/")
def formateur_list(request):
    formulaires = Formulaire.objects.all()
    return render(request, 'formateur_list.html', {'formulaires': formulaires})

@login_required(login_url="/admin/login/?next=/formateur/<str:id_formulaire>/")
def formateur_details(request, id_formulaire):
    reponses = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire)
    total_reponses = reponses.count()
    moy_progression = reponses.aggregate(avg_progression=Avg('progression'))['avg_progression'] or 0
    count_difficulte = defaultdict(int)
    count_maitrise = defaultdict(int)
    
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

def etudiant_login(request):
    if not request.COOKIES.get('JWT'):
        form = LoginForm()
        message = ''
        if request.method == 'POST':   
            form = LoginForm(request.POST)    
            if form.is_valid():
                username = form.cleaned_data['username']
                password = utility.hash_password(form.cleaned_data['password'])

                try:
                    Etudiant.objects.get(username=username, password=password)
                    token = utility.generate_jwt(username)
                    reponse = HttpResponseRedirect('/etudiant/')
                    reponse.set_cookie('JWT', token)
                    return reponse
                except Etudiant.DoesNotExist:
                    message = 'Utilisateur ou mot de passe incorrect !'

        return render(request, 'etudiant_login.html', {
            'form' : form, 
            'message' : message })
    else:
        return HttpResponse("Déjà connecté<br/><a href='/etudiant/'>Formulaires</a><br/><a href='/logout/'>Logout</a>")

def etudiant_logout(request):
    try:
        reponse = redirect('/login/')
        reponse.delete_cookie('JWT')
        return reponse
    except:
        return HttpResponse("Une erreur s'est produite")
    
def etudiant_list(request):
    try:
        token = request.COOKIES.get('JWT')
        utility.decode_jwt(token)
        if token:
            formulaires = Formulaire.objects.filter(ouvert=True)
            return render(request, 'etudiant_list.html', {'formulaires': formulaires})
        else:
            return HttpResponseRedirect('/login/')
    except jwt.ExpiredSignatureError:
        reponse = HttpResponseRedirect('/login/')
        reponse.delete_cookie('JWT')
        return reponse
    except jwt.InvalidTokenError:
        reponse = HttpResponseRedirect('/login/')
        reponse.delete_cookie('JWT')
        return reponse

def etudiant_formulaire(request, id_formulaire):
    try:
        token = request.COOKIES.get('JWT')
        payload = utility.decode_jwt(token)
        username = payload['username']
        if username:            
            formulaire = Formulaire.objects.filter(id_formulaire=id_formulaire).first()
            if formulaire.ouvert:
                reponse = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire, numero_etudiant__username__iexact=username).first()
                if not reponse:
                    etudiant = Etudiant.objects.filter(username=username).first()
                    init = ReponsesFormulaire.objects.create(id_formulaire_id=id_formulaire, numero_etudiant_id=etudiant.numero_etudiant, date_access=timezone.now())
                    init.save()
                    reponse = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire, numero_etudiant__username__iexact=username).first()
                urlAPI = env.API_FLASK
                return render(request, 'etudiant_formulaires.html', {
                    'formulaire' : formulaire,
                    'reponse' : reponse,
                    'urlAPI' : urlAPI})
            else:
                return HttpResponse("Formulaire <span style='color: rgb(224, 42, 42);''>fermé</span>. <br/><a href='/etudiant/'>Retour</a>")
        else:
            return HttpResponseRedirect('/login/')
    except jwt.ExpiredSignatureError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse
    except jwt.InvalidTokenError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse
    except KeyError:
        reponse = HttpResponseRedirect('/logout/')
        return reponse