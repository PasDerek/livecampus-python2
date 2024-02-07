from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from collections import defaultdict
from .models import Formulaire
from .models import ReponsesFormulaire

def list_forms_admin(request):
    formulaires = Formulaire.objects.all()
    return render(request, 'formulaires_list.html', {'formulaires': formulaires})

def detail_forms_admin(request, id_formulaire):
    formulaire = get_object_or_404(Formulaire, id_formulaire=id_formulaire)
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
    
    for key,value in count_difficulte.items():
        print(f'{key} : {value}')

    return render(request, 'formulaires_details.html', {
        'formulaire': formulaire,
        'reponses': reponses,
        'total_reponses': total_reponses,
        'moy_progression': moy_progression,
        'count_difficulte' : count_difficulte.items(),
        'count_maitrise' : count_maitrise.items()
    })