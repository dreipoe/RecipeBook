from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from .models import Receipt


def index(request: WSGIRequest):
    return render(request, "main.html", {'title': "Книга рецептов", 'items': Receipt.objects.all()})


def detail(request: WSGIRequest, idx: int):
    item = get_object_or_404(Receipt, pk=idx)
    ingredients = item.get_ingredients()

    return render(request, "detail.html", {"item": item, "ingredients": ingredients})
