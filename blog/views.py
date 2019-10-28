from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Articles, Users

def index(request):
    articles = Articles.objects.filter(active=0)[0]
    print(articles)
    return render(request, 'index.html', {'articles': articles})

def affiche_article(request):
    articles = Articles.objects.get(active = 1)
    print(articles)

def register_page(request):
    return render(request, 'login/register_page.html')

def register_user(request):
    use_verif = ''
    if request.method == "post":
        nom = request.POST['nom']
        postnom = request.POST['postnom']
        role = request.POST['role']
        gender = request.POST['genre']
        email = request.POST['email']
        phone = request.POST['telephone']
        mail = request.POST['email']
        avatar = request.POST['avatar']


        if request.POST["pass1"] != request.POST["pass2"]:
            messages.add_message(request, messages.ERROR, "Retapez le mot mot de passe conforme au premier")
            return redirect('login/register_page.html')
        else:
            password = request.POST['pass1']
            use_verif = Users.objects.get(firstname=request.POST['nom'])  # , email = request.POST['email'])
            print(use_verif)
    if len(use_verif) == 0:
        messages.add_message(request, messages.ERROR, "Utilisateur deja existant")
        return redirect('login/register_page.html')
    else:
        return render(request, '/')


    return redirect(request, 'index.html')

def login_page(request):
    return render(request, 'login/login.html')

def login_user(request):
    try:
        user = Users.objects.get(firstname = request.POST['usn'])
        if user.password == request.POST['pwd']:
            request.session['id']= user.id
            request.session['name']= user.firstname
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Coordonnees non trouvees")
            return render(request, 'login/login.html')
    except ValueError:
        messages.add_message(request, messages.ERROR, "Coordonnees non trouvees")
        return render(request, 'login/login.html')

@login_required(login_url="login_page")
def logout_user(request):
    logout(request)
    return redirect("/")