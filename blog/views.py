from django.shortcuts import render, redirect
from django import http
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Articles, Users, Roles, Commentaires, Newsletter
from datetime import date
import sys
from django.core.files import *
from .functions import *

def index(request):
    return render(request, "index.html")

def articles(request):
    #articles = Articles.objects.all()
    articles = active_articles()
    return render(request, "recent.html", {"all": articles})


def read_article(request, id):
    all_articles = active_articles()
    article = Articles.objects.get(pk = id)
    commentaire = Commentaires.objects.filter(article=article.id)
    return render(request, 'articles.html', {'commentaires': commentaire, 'r_article': article, 'all': all_articles})


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
    active_article = active_articles()
    disactive_article = disactive_articles()
    comments = all_commentaires()
    abonnes = all_newsletters()
    ip_address = http.HttpResponse(request.META["REMOTE_ADDR"])
    ip_address = ip_address
    return render(request, 'admin/main_dashboard.html', locals())



def create_article_page(request):
    categories = all_categories()
    return render(request, 'article/create_article_page.html', locals())



def create_article(request):
    if request.method == "POST":
        if Users.objects.get(pk=request.POST['user']):
            user = Users.objects.get(pk=request.POST['user'])
        else:
            print('utilisateur non trouve')

        if Categories.objects.get(pk=request.POST['category']):
            category = Categories.objects.get(pk=request.POST['category'])
        else:
            print('categorie non trouve')
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        state = request.POST['state']


        title = title,
        content = content,
        image = image,
        state = state,
        return HttpResponse('')

def create_art(request):
    if request.method == "POST":
        #handling the user input
        if Users.objects.get(pk=request.POST['usert']):
            user = Users.objects.get(pk=request.POST['usert'])
        else:
            print('utilisateur non trouve')
        #handling the category input
        if Categories.objects.get(pk=request.POST['category']):
            category = Categories.objects.get(pk=request.POST['category'])
        else:
            print('categorie non trouve')
        # handling the sendable input
        if request.POST.get("sendable"):
            sendable = True
        else:
            sendable = False
        #other input
        title = request.POST['title']
        content = request.POST['content']
        state = request.POST['state']
        imagette = request.FILES['imagette']
    else:
        print("aucune donnée transmise")
    print(title, content, user, category, state, sendable)
    print(imagette)
    Articles.objects.create(
        user = user,
        title = title,
        content = content,
        categorie = category,
        state = state,
        sendable = sendable,
        image_article = imagette
    )
    return redirect("/create_article_page")

def edit_article_page(request, id):
    get_article = Articles.objects.get(pk=id)
    get_category = all_categories
    return render(request, 'article/edit_article_page.html', locals())

def edit_article(request, id):
    article = Articles.objects.get(pk=id)
    if request.method == "POST":
        article.user = Users.objects.get(pk=request.POST['user'])
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.category = request.POST['category']
        article.state = request.POST['state']
        if request.POST.get("sendable"):
            article.sendable = True
        else:
            article.sendable= False

        if request.POST['imaget']:
            print("image fournie")
            article.image_article = request.FILES['imaget']
        else:
            print("image originale")
            article.image_article = Articles.objects.get(pk=id).image_article
        article.save()
    return redirect("/admin")

def corbeille_article(request, id):
    article = Articles.objects.get(pk=id)
    article.active = False
    article.save()
    return redirect("/admin")

def restore_article(request, id):
    article = Articles.objects.get(pk=id)
    article.active = True
    article.save()
    return redirect("/admin")