from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name="home"),
    path('authenticate/login/', views.user_login_view, name='user_login'),
]