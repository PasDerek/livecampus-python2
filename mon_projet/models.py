from django.db import models
from django.utils import timezone
from .utility import *

# Table mon_projet_tudiant
class Etudiant(models.Model):
    numero_etudiant = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = 'Etudiant'
        verbose_name_plural = 'Etudiants'

    # Sauvegarder = Hash mot de passe avec fonction bcrypt
    def save(self, *args, **kwargs):
        self.password = hash_password(self.password)
        super().save(*args, **kwargs)

# Table mon_projet_formulaire
class Formulaire(models.Model):
    id_formulaire = models.AutoField(primary_key=True)
    nom_formulaire = models.CharField(max_length=50, null=False)
    ouvert = models.BooleanField(default=True)
    date_ouverture = models.DateTimeField(auto_now_add=True, editable=False)
    date_fermeture = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Formulaire'
        verbose_name_plural = 'Formulaires'

    # Sauvegarder = Si formulaire ouvert, écraser date ouverture et supprimer heure fermeture. Si formulaire fermé, écrire la date de fermeture
    def save(self, *args, **kwargs):
        if self.ouvert:
            self.date_ouverture = timezone.now()
            self.date_fermeture = None
        elif self.pk:
            self.date_fermeture = timezone.now()
        super().save(*args, **kwargs)

# Table mon_projet_reponsesformulaire
# 2 foreign key : id_formulaire de Formulaire et numero_etudiant de Etudiant
class ReponsesFormulaire(models.Model):
    id_formulaire = models.ForeignKey(Formulaire, on_delete=models.CASCADE)
    numero_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    progression = models.IntegerField(default=0)
    difficulte = models.CharField(max_length=50, default='Vide')
    maitrise = models.CharField(max_length=50, default='Vide')
    date_access = models.DateTimeField(null=True, blank=True, editable=False)