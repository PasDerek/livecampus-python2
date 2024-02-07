from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulaire

def list_forms_admin(request):
    formulaires = Formulaire.objects.all()
    return render(request, 'formulaires_list.html', {'formulaires': formulaires})