"""
URL configuration for mon_projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil avec lien vers certaines des autres pages
    path('', views.home),
    # Vue admin par défaut
    path('admin/', admin.site.urls),
    # Etudiants - Login et logout
    path('login/', views.etudiant_login),
    path('logout/', views.etudiant_logout),
    # Formateurs - Pages de listing et de détail
    path('formateur/', views.formateur_list),
    path('formateur/<str:id_formulaire>/', views.formateur_details),
    # Etudiants - Pages de listing et de détails
    path('etudiant/', views.etudiant_list),
    path('etudiant/<str:id_formulaire>/', views.etudiant_formulaire),
]
