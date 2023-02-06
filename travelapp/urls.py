from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.showpost, name='showpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('user/<str:username>/', views.user_profile, name='user_profile')
]
