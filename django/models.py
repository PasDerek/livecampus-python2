from django.db import models
from django.utils import timezone
from .utility import *

class Etudiant(models.Model):
    numero_etudiant = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)

    def save(self, *args, **kwargs):
        self.password = hash_password(self.password)
        super().save(*args, **kwargs)

class Formulaire(models.Model):
    id_formulaire = models.AutoField(primary_key=True)
    nom_formulaire = models.CharField(max_length=50, null=False)
    ouvert = models.BooleanField(default=True)
    date_ouverture = models.DateTimeField(auto_now_add=True, editable=False)
    date_fermeture = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Formulaire'
        verbose_name_plural = 'Formulaires'

    def save(self, *args, **kwargs):
        if self.ouvert:
            self.date_ouverture = timezone.now()
            self.date_fermeture = None
        elif self.pk:
            self.date_fermeture = timezone.now()
        super().save(*args, **kwargs)

class ReponsesFormulaire(models.Model):
    id_formulaire = models.ForeignKey(Formulaire, on_delete=models.CASCADE)
    numero_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    progression = models.IntegerField(default=0)
    difficulte = models.CharField(max_length=50, default='Vide')
    maitrise = models.CharField(max_length=50, default='Vide')
    date_access = models.DateTimeField(null=True, blank=True, editable=False)