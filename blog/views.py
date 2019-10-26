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