from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('<int:contato_id>', views.verContato, name='verContato'),
]
