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
    # была идея использовать pymorphy2, но разбираться было долго, а времени не было
    name = models.CharField(max_length=32, unique=True, verbose_name='Название ')
    name_case_1 = models.CharField(max_length=32, null=True, blank=True, verbose_name='Название (например, 2 ложки)')
    name_case_2 = models.CharField(
        max_length=32, null=True, blank=True, verbose_name='Название (например, 5 ложек)'
    )

    def get_inflected_name(self, n: int):
        name = self.name_case_2 if self.name_case_2 is not None else self.name
        if n // 10 % 10 != 1:
            last_digit = n % 10
            if last_digit == 1:
                name = self.name
            elif last_digit in range(2, 5):
                name = self.name_case_1 if self.name_case_1 is not None else self.name

        return name


class Ingredient(NamedModel):
    class Meta:
        app_label = "main"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    name = models.CharField(max_length=32, unique=True, verbose_name='Название в родительном падеже')


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
        n = 500
        return f"{self.definition[0:n]}..." if len(self.definition) > n else self.definition

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
        n = self.n
        return f"{n} {self.measure.get_inflected_name(n)} {self.ingredient}"
