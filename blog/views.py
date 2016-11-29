'''
FileName: blog/views.py
'''
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Article, Category


class IndexView(ListView):
    """首页"""
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(status='p').order_by('-pub_date')[:5]


class ArticleDetailView(DetailView):
    """文章详情"""
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'articles'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        if obj.status == 'p':
            obj.viewed()
            return obj


class CategoryView(ListView):
    """
    分类页
    """
    template_name = 'blog/category.html'
    context_object_name = 'articles'

    def get_queryset(self):
        category_id = int(self.kwargs['category_id'])
        if category_id == 0:
            articles = Article.objects.filter(
                category__isnull=True, status='p')
        else:
            articles = Article.objects.filter(category=category_id, status='p')
            return articles


class TagView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.objects.filter(
            tags=self.kwargs['tag_id'], status='p')
        return articles
