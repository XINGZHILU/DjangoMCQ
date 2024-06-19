from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login.html'),
    path('register/',views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('practice/physics/', views.physics, name='logout'),
    path('practice/economics/', views.economics, name='logout'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('account/', views.account, name='account'),
    path('customised/', views.customised, name='customised'),
    #path('about/', views.about, name='about'),
    path('downloaddb/', views.database, name='database'),
]
