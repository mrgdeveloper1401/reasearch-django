from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # path('login/', views.LoginUserView.as_view(), name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
]
