from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Photos


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class PhotoForm(ModelForm):
    class Meta:
        model = Photos
        fields = ['avatar']
