from django.contrib import admin
from django.urls import path,include
from basicApp import views

app_name='basicApp'

urlpatterns = [
    path ('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),



]