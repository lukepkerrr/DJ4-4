from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Data


def articles_list(request):

    articles = Article.objects.all()

    data = Data.objects.all()


    template = 'articles/news.html'
    context = {
        'object_list': articles,
        'data': data
    }
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
