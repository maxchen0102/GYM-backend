
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('enroll/', views.enroll, name='enroll'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('introduce_page/', TemplateView.as_view(template_name='introduce_page.html'), name='introduce_page'),
    path('test/', views.test, name='test'),
    path('certificate/', views.certificate, name='certificate'),
]