from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('login/', views.loginUser, name="login-user"),
    path('register/', views.registerUser, name="register-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('photo-list/', views.photoList, name="photo-list"),
     path('upload-photo/', views.uploadPhoto, name="upload-photo"),
]
