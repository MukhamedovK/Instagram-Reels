from django.urls import path
from . import views


urlpatterns = [
    path('api/accounts/register/', views.RegisterUserAPIView.as_view(), name='APIregister'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
]

