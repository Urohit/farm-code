from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='/'),
    path('login', views.login, name='login'),
    path('user_panel', views.user_panel, name='user_panel'),
    path('logout', views.logout, name='logout'),
    path('navbar', views.navbar, name='navbar'),
    path('browse', views.browse, name='browse'),
    path('investor', views.investor_page, name='investor'),
    path('investor_detail/<str:pk>/', views.investor_detail, name='investor_detail'),
    path('create_product', views.create_product, name='create_product'),
]
