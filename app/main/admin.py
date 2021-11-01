from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Measure)
admin.site.register(Ingredient)
admin.site.register(Receipt)
admin.site.register(ReceiptItem)
