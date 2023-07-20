from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'pages/about.html'
    return render(request, template_name)


def rules(request: HttpRequest) -> HttpResponse:
    template_name: str = 'pages/rules.html'
    return render(request, template_name)
