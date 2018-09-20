from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, "articles/article_list.html", context)


def article_full(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article' : article
    }
    return render(request, "articles/article_full.html", context)


@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')