from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name="home"),
<<<<<<< HEAD
    path('authenticate/login/', views.user_login_view, name='user_login'),
=======
    path('user/login/', views.user_login_view, name='user_login'),
>>>>>>> 8e94b5b (for infopuhali)
]