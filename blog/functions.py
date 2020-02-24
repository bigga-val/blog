from django.shortcuts import render

from .models import Users, Articles, Roles, Commentaires, Categories, Newsletter


def all_articles():
    articles = Articles.objects.all()
    return articles

def active_articles():
    articles = Articles.objects.filter(active=True).all()
    return articles

def disactive_articles():
    articles = Articles.objects.filter(active=False).all()
    return articles

def all_users():
    users = Users.objects.all()
    return users

def all_roles():
    roles = Roles.objects.all()
    return roles

def all_commentaires():
    comments = Commentaires.objects.all()
    return comments

def all_newsletters():
    newsletters = Newsletter.objects.all()
    return newsletters

def all_categories():
    categories = Categories.objects.all()
    return categories




