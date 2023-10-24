from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm
from .models import User


# class LoginUserView(auth_views.LoginView):
#     template_name = 'accounts/login.html'
#     next_page = reverse_lazy('homes:home')
    
    
class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('accounts:login')


class UserLoginView(View):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in!', 'success')
                return redirect('homes:home')
            else:
                messages.error(request, 'Invalid username and/or password', 'warning')
                return redirect('accounts:login')
        return render(request, self.template_name, {'form': form})
                
            
class UserRegisterView(View):
    from_class = UserRegisterForm
    template_name = 'accounts/user_register.html'
    
    def get(self, request, *args, **kwargs):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                cd['email'],
                cd['mobile_phone'],
                cd['password']
            )
            messages.success(request, 'You are now registered and can log in','success')
            return redirect('homes:home')
        return render(request, self.template_name, {'form': form})
    
