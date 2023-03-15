from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.UpdateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.DeleteRoom,name='delete-room'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('delete-message/<str:pk>/',views.DeleteMessage,name='delete-message'),
    path('profile/<str:pk>/',views.userProfile,name='user-profile'),
    path('update-user',views.updateUser,name='update-user'),
    path('topics',views.topicsPage,name='topics'),
    path('activity',views.activityPage,name='activity'),
]