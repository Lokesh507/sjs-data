from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_page', views.data_page, name='data_page'),
    path('bill_page', views.bill_page, name='bill_page'),
    path('login_page', views.login_page, name='login_page'),
    path('logout_page', views.logout_page, name='logout_page')
]
