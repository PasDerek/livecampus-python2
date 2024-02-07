from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from collections import defaultdict
from .models import Etudiant
from .models import Formulaire
from .models import ReponsesFormulaire

def list_forms_admin(request):
    formulaires = Formulaire.objects.all()
    return render(request, 'formulaires_list.html', {'formulaires': formulaires})

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

def forms_etudiant(request, id_formulaire):
    formulaire = Formulaire.objects.filter(id_formulaire=id_formulaire)
    print(formulaire[0].ouvert)
    return render(request, 'formulaires_etudiant.html', {'id_formulaire' : id_formulaire})