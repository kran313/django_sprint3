from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog.models import Post, Category
from datetime import datetime


def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'blog/index.html'
    post_list = Post.objects.filter(pub_date__lt=datetime.now(),
                                is_published=True,
                                category__is_published=True)[:5]
    context: dict = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template_name: str = 'blog/detail.html'
    posts = Post.objects.get(pk=id)
    context: dict = {'post': posts}
    return render(request, template_name, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template_name: str = 'blog/category.html'

    post_list = Category.objects.filter(slug=category_slug).select_related(
        'posts'
        ).filter(is_published=True,
                 pub_date__lt=datetime.now())

    """post_list = Post.objects.select_related(
        'posts'
        ).filter(slug=category_slug,
                 is_published=True,
                 pub_date__lt=datetime.now())"""
    context: dict = {'post_list': post_list}
    return render(request, template_name, context)
