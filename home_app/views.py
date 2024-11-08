from django.shortcuts import render
from blog_app.models import Article


def home(request):
    articles = Article.custom_manager.all()
    return render(request, 'home_app/index.html', context={'Articles': articles})


def sidebar(requset):
    data = {'name':'alireza'}
    return render(requset, 'includes/sidebar.html', context=data)
