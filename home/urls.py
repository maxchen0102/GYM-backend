
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),

    path('introduce_page/', views.introduce_page, name='introduce_page'),
    path('detail/', views.detail, name='detail'),
    path('certificate/', views.certificate, name='certificate'),
    path('permission_denied/', TemplateView.as_view(template_name='permission_denied.html'), name='permission_denied'),

]