from . import views
from django.urls import path

urlpatterns = (
    path('', views.index, name='index'),
    path('receipt/<int:idx>', views.detail, name='detail')
)
