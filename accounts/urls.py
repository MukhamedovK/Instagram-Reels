from django.urls import path
from . import views


urlpatterns = [
    path('api/accounts/register/', views.RegisterUserAPIView.as_view(), name='APIregister'),
    # path('api/accounts/login/', views.LoginUserAPIView.as_view(), name='APIlogin'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.LogoutUserAPIView.as_view(), name='logout_page'),
]

