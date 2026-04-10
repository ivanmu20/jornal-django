from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {'article': article})


def comments(request, id):
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(article=article)

    if request.method == "POST":
        text = request.POST.get("text")
        Comment.objects.create(article=article, text=text)
        return redirect('comments', id=id)

    return render(request, 'comments.html', {
        'article': article,
        'comments': comments
    })