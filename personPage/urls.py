
from django.urls import path
from . import views


urlpatterns = [
    path('', views.personPage, name='personPage'),
    path('get_category/', views.getPersonalCategory, name='category'),
    path('add_category/', views.addCategory, name='add_category'),
    path('delete_category/', views.deleteCategory, name='delete_category'),
    path('update_category/', views.updateCategory, name='update_category'),
]