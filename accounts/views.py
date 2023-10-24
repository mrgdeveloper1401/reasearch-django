from django.shortcuts import render
from django.views import View
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# class LoginUserView(auth_views.LoginView):
#     template_name = 'accounts/login.html'
#     next_page = reverse_lazy('homes:home')
    
    
class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('accounts:login')


class UserLoginView(View):
    template_name = ''
    form_class = ''
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        pass
    
    
