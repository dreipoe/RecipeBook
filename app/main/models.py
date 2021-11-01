from django.core.paginator import Paginator, Page
from django.db import models


class Measure(models.Model):
    """Единицы измерения"""
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')


class Ingredient(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')


class Receipt(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='Название')
    definition = models.TextField(max_length=4000, verbose_name='Описание')

    @staticmethod
    def get_page(page) -> Page:
        """
        Возвращает страницу из списка рецептов

        :param page: Номер страницы
        """
        items = None
        objects = Receipt.objects.order_by('pk')
        if objects.count() > 0:
            paginator = Paginator(objects, 20)
            items = paginator.page(page)

        return items


class ReceiptItem(models.Model):
    """Строка в рецепте, например: '2 чайные ложки соли'"""
    n = models.IntegerField(verbose_name='Кол-во')
    measure = models.ForeignKey(to=Measure, on_delete=models.RESTRICT, verbose_name='Единица измерения')
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.RESTRICT, verbose_name='Ингредиент')
    receipt = models.ForeignKey(to=Receipt, on_delete=models.RESTRICT, verbose_name='Рецепт')
