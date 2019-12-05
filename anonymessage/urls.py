from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('authenticate/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('message-to/<slug:username>', views.send_message, name='private_link'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]