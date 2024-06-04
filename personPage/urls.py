
from django.urls import path
from . import views


urlpatterns = [
    path('', views.personPage, name='personPage'),
    path('category/', views.getPersonalCategory, name='category'),
]