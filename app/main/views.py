from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Receipt


def index(request: WSGIRequest):
    return render(request, "main.html", {'title': "Книга рецептов", 'items': Receipt.objects.all()})


def view(request: WSGIRequest, idx: int):
    pass
