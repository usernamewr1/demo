from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.reg_user, name='reg'),
    path('login', views.log_user, name='login'),
    path('newpost', views.new_post, name='newpost'),
    path('logout', views.logout_user, name='logout'),
    path('<int:pk>', views.PostDetail.as_view(), name='detail'),
]