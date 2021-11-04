from django.core.paginator import Paginator, Page
from django.db import models


class NamedModel(models.Model):
    class Meta:
        abstract = True

    name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert(isinstance(self.name, str), TypeError("self.name is not char field"))

    def __str__(self):
        return self.name


class Measure(NamedModel):
    class Meta:
        app_label = "main"
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"

    """Единицы измерения"""
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')


class Ingredient(NamedModel):
    class Meta:
        app_label = "main"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    name = models.CharField(max_length=32, unique=True, verbose_name='Название')


class Receipt(NamedModel):
    class Meta:
        app_label = "main"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

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

    def cut_definition(self):
        return f"{self.definition[0:450]}..."

    def get_ingredients(self):
        return ReceiptItem.objects.filter(receipt=self.id)


class ReceiptItem(models.Model):
    class Meta:
        app_label = "main"
        verbose_name = "Ингредиент в рецепте"
        verbose_name_plural = "Ингредиенты в рецепте"

    n = models.IntegerField(verbose_name='Кол-во')
    measure = models.ForeignKey(to=Measure, on_delete=models.RESTRICT, verbose_name='Единица измерения')
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.RESTRICT, verbose_name='Ингредиент')
    receipt = models.ForeignKey(to=Receipt, on_delete=models.RESTRICT, verbose_name='Рецепт')

    def __str__(self):
        return f"{self.n} {self.measure} {self.ingredient}"
