from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View

# Create your views here.
def index(request: WSGIRequest):
    return render(request, "main.html", {'title': "Книга рецептов"})
