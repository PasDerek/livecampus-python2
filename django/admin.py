from django.contrib import admin
from .models import Etudiant
from .models import Formulaire

admin.site.register(Etudiant)
admin.site.register(Formulaire)