from django.db import models
from datetime import date
from django import forms

class Roles(models.Model):
    name = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

class Users(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE())
    gender = models.CharField(max_length=1)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(null=True)
    adhesion_date = models.DateField()
    active = models.BooleanField(default=True, required=False)

class Categories(models.Model):
    name = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

class Articles(models.Model):
    user = models.ForeignKey(Users, unique=True)
    categorie = models.ManyToManyField(Categories)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, default = 'opened') #opened or closed
    active = models.BooleanField(default=True)

class Commentaires(models.Model):
    user = models.ForeignKey(Users)
    pseudo = models.CharField(max_length=20)
    article = models.ForeignKey(Articles)
    commentaire = models.CharField(max_length=1000)

class Newsletter(models.Model):
    mail = models.EmailField()
    inscription_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)