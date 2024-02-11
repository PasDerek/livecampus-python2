from django.contrib import admin
from .models import Etudiant
from .models import Formulaire

# Ajout des modèles a la vue admin
# Penser à rajouter dans INSTALLED_APPS de 'settings.py' le nom du dossier 'projet'
admin.site.register(Etudiant)
admin.site.register(Formulaire)