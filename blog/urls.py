"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recent', views.articles),
    path('read_article/<int:id>', views.read_article),
    path('login_page', views.login_page),
    path('login_user', views.login_user),
    path('logout_user', views.logout),
    path('register_page', views.register_page),
    path('register', views.register_user),
    path('add_comment', views.commenter),
    path('abonne', views.add_abonne),
    path('create_abonne', views.create_abonne),
    path('admin', views.main_dashboard),
    path('create_article_page', views.create_article_page),

]
