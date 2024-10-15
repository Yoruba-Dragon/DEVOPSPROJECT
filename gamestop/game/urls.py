from django.urls import path
from . import views

urlpatterns = [

    #Authentication
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.password_change, name='change_password'),

    path('', views.game_index, name='home'),
    path('resturants/', views.resturant_list, name='resturant_list'),
    path('game/', views.store_list, name='store_list'),
    #path('add/', views.add_game, name='add_game'),
    #path('<str:pk>/edit/', views.edit_game, name='edit_game'),
    #path('<str:pk>/delete/', views.delete_game, name='delete_game'),
]
