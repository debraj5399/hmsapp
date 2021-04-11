from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name = 'home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forgetpass', views.forgetpass, name='forgetpass'),
    path('logout', views.login, name='logout')
]

