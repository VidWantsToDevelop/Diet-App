from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<str:user>', views.profile, name='profile'),
    path('create_day', views.create_day, name='createDay'),
]