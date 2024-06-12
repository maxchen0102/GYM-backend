
from django.urls import path
from . import views


urlpatterns = [
    path('', views.personPage, name='personPage'),
    path('test/<str:name>', views.test, name='test'),

    # categories
    path('get_category/', views.getPersonalCategory, name='category'),
    path('add_category/', views.addCategory, name='add_category'),
    path('delete_category/', views.deleteCategory, name='delete_category'),
    path('update_category/', views.updateCategory, name='update_category'),

    # items
    path('add_item/', views.add_item, name='add_item'),
    path('get_items/', views.get_items, name='items'),
    path('delete_item/', views.delete_item, name='delete_item'),
    path('update_item/', views.update_item, name='update_item'),

    # Lists
    path('get_record_list/', views.get_record_list, name='add_record_list'),
    path('add_record_list/', views.add_record_list, name='add_record_list'),
    path('delete_record_list/', views.delete_record_list, name='delete_record_list'),
    path('update_record_list/', views.update_record_list, name='update_record_list'),


]