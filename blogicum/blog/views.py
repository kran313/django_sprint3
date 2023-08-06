from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
import datetime


NUMBER_OF_POSTS_ON_MAIN_PAGE: int = 5

def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category'
    ).filter(pub_date__lte=datetime.datetime.now(),
             is_published=True,
             category__is_published=True)[:NUMBER_OF_POSTS_ON_MAIN_PAGE]
    context: dict = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    template_name: str = 'blog/detail.html'

    posts = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True
    )

    context: dict = {'post': posts}
    return render(request, template_name, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    template_name: str = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.select_related(
        'category'
    ).filter(category=category,
             is_published=True,
             pub_date__lte=datetime.datetime.now())

    context: dict = {'post_list': post_list}
    return render(request, template_name, context)
