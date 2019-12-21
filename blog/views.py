from django.shortcuts import render, redirect
from django import http
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Articles, Users, Roles, Commentaires, Newsletter
from datetime import date
import sys
from .functions import *

def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Articles.objects.all()
    return render(request, "recent.html", {"all": articles})


def read_article(request, id):
    all_articles = Articles.objects.all()
    article = Articles.objects.get(pk = id)
    commentaire = Commentaires.objects.filter(article=article.id)
    return render(request, 'articles.html', {'commentaires': commentaire, 'r_article': article, 'all': all_articles})

def affiche_article(request):
    articles = Articles.objects.get(active = 1)
    print(articles)

def register_page(request):
    return render(request, 'login/register_page.html')

def register_user(request):
    use_verif = ''
    #if request.method == "post":
    nom = request.POST['nomf']
    postnom = request.POST['postnom']
    role = Roles.objects.get(pk = 1)
    genre = request.POST['sexe']
    mail = request.POST['email']
    phone = request.POST['telephone']
    avatar = request.POST['avatar']
    adhesion_date = date.today()

        #verifying if passwords fields are equal
    if request.POST["pass1"] != request.POST["pass2"]:
        messages.add_message(request, messages.ERROR, "Retapez le mot mot de passe conforme au premier")
        return redirect('/register_page')
    else:
        try:
            password = request.POST['pass1']
            use_verif = Users.objects.get(firstname=request.POST['nomf'])  # , email = request.POST['email'])

        except:
            pass

    if use_verif:
        #print(len(use_verif))
        messages.add_message(request, messages.ERROR, "Utilisateur deja existant")
        return redirect('/register_page')
    else:
        user = Users(firstname=nom, lastname=postnom, role=role, gender=genre, email=mail, phone=phone, image=avatar,
                     adhesion_date=adhesion_date, password=password)
        user.save()
        return redirect('/recent')


def login_page(request):
    return render(request, 'login/login.html')

def login_user(request):
    #try:
    print(request.POST['usn'])
    user = Users.objects.get(firstname = request.POST['usn'])
    print(user.firstname)
    if user.password == request.POST['pwd']:
        request.session['id']= user.id
        request.session['name']= user.firstname
        login(request, user)
        print(user.firstname)
        print(user.password)
        print(request.POST['pwd'])
        return redirect('/recent')
    else:
        messages.add_message(request, messages.ERROR, "Utilisateur non reconnu")
        return render(request, '/login/login.html')
    #except:
     #   messages.add_message(request, messages.ERROR, "Coordonnees non trouvées, Veuillez vous inscrire")
      #  #return redirect('/articles')
       # return render(request, 'login/login.html')

@login_required(login_url="/login_page")
def logout_user(request):
    logout(request)
    return redirect("/recent")



def commenter(request):
    print(request.POST['utilisateur'])
    print(request.POST['article'])
    print(request.POST['commentaire'])
    try:
        use = Users.objects.get(pk = request.POST['utilisateur'])
    except:
        messages.add_message(request, messages.ERROR, "veuillez vous connecter pour commenter {}".format(sys.exc_info()[0]))
        return redirect("recent")

    art = Articles.objects.get(pk = request.POST['article'])

    commentair = request.POST['commentaire']
    comment = Commentaires(user = use, article = art, commentaire = commentair)
    #print(comment)
    comment.save()
    return redirect('read_article/'+ request.POST['article'])


def add_abonne(request):
    mail = request.POST['email']
    email_user = Newsletter(mails =mail)
    email_user.save()
    return redirect("/")

def create_abonne(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        Newsletter.objects.create(
            mails = mail
        )
        return HttpResponse('')



def main_dashboard(request):
    articles = all_articles()
    comments = all_commentaires()
    abonnes = all_newsletters()
    ip_address = http.HttpResponse(request.META["REMOTE_ADDR"])
    ip_address = ip_address
    return render(request, 'admin/main_dashboard.html', locals())

def create_article_page(request):
    return render(request, 'article/create_article_page.html')