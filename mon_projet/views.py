from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from collections import defaultdict
from .models import Etudiant
from .models import Formulaire
from .models import ReponsesFormulaire
from .forms import LoginForm
from . import utility

@login_required(login_url="/admin/login/?next=/formateur/")
def list_forms_admin(request):
    formulaires = Formulaire.objects.all()
    return render(request, 'formulaires_list.html', {'formulaires': formulaires})

@login_required(login_url="/admin/login/?next=/formateur/<str:id_formulaire>/")
def detail_forms_admin(request, id_formulaire):
    reponses = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire)
    total_reponses = reponses.count()
    moy_progression = reponses.aggregate(avg_progression=Avg('progression'))['avg_progression'] or 0
    count_difficulte = defaultdict(int)
    count_maitrise = defaultdict(int)

    print(reponses.values())
    
    for reponse in reponses:
        if reponse.difficulte:
            count_difficulte[reponse.difficulte] += 1
        if reponse.maitrise:
            count_maitrise[reponse.maitrise] += 1

    return render(request, 'formulaires_details.html', {
        'id_formulaire' : id_formulaire,
        'reponses': reponses,
        'total_reponses': total_reponses,
        'moy_progression': moy_progression,
        'count_difficulte' : count_difficulte.items(),
        'count_maitrise' : count_maitrise.items()
    })

def login_etudiant(request):
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
                print(type(token))
                response = HttpResponseRedirect('/login')
                response.set_cookie('JWT', token)
                return response
            except Etudiant.DoesNotExist:
                message = 'Utilisateur ou mot de passe incorrect !'

    return render(request, 'login.html', {
        'form' : form, 
        'message' : message })

def forms_etudiant(request, id_formulaire):
    token = request.COOKIES.get('JWT')
    if token:
        payload = utility.decode_jwt(token)
        username = payload['username']
        
        formulaire = Formulaire.objects.filter(id_formulaire=id_formulaire)
        if formulaire[0].ouvert:
            reponses = ReponsesFormulaire.objects.filter(id_formulaire=id_formulaire)
            return render(request, 'formulaires_etudiant.html', {
                'id_formulaire' : id_formulaire,
                'reponses': reponses})
        else:
            return HttpResponse('Formulaire <span style="color: rgb(224, 42, 42);">fermé</span>')
    else:
        return HttpResponse('Merci de vous connecter')