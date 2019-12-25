from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser

class Roles(models.Model):
    name = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Users(AbstractBaseUser):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(null=True)
    adhesion_date = models.DateField()
    password = models.CharField(max_length=30, null=False, default='article')
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.id)

class Categories(models.Model):
    name = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Articles(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    categorie = models.ForeignKey(Categories, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_article = models.ImageField(upload_to="")
    creation_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=10, default = 'opened') #opened or closed
    sendable = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Commentaires(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.PROTECT)
    commentaire = models.TextField()


    def __str__(self):
        return str(self.id)

class Newsletter(models.Model):
    mails = models.EmailField()
    inscription_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.id)

class Visitors(models.Model):
    ip_address = models.GenericIPAddressField()
    page_visited = models.TextField()
    date_visite = models.DateTimeField(default=datetime.now)