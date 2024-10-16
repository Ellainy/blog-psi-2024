from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('dirturbios/', views.diturbios, name = 'disturbios'),
    path('ajuda/', views.ajuda, name = 'ajuda')
]