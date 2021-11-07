from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from .models import Receipt, ReceiptItem, Ingredient


def index(request: WSGIRequest):
    receipt_name = request.GET.get("receipt")
    ingredient_name = request.GET.get("ingredient")

    receipts = Receipt.objects.all()
    if ingredient_name not in (None, ''):
        receipts = receipts.filter(
            pk__in=ReceiptItem.objects.filter(
                ingredient__in=Ingredient.objects.filter(name__icontains=ingredient_name)
            ).values_list("receipt_id")
        )
    if receipt_name not in (None, ''):
        receipts = receipts.filter(name__icontains=receipt_name)

    return render(request, "main.html", {
        'title': "Книга рецептов",
        'items': receipts,
        'receipt_name': receipt_name,
        'ingredient_name': ingredient_name
    })


def detail(request: WSGIRequest, idx: int):
    item = get_object_or_404(Receipt, pk=idx)
    ingredients = item.get_ingredients()

    return render(request, "detail.html", {"item": item, "ingredients": ingredients})
