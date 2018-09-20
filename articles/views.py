from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms


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
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save to database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else: #GET
        form = forms.CreateArticle()
    context = {
        'form' : form
    }
    return render(request, 'articles/article_create.html', context)