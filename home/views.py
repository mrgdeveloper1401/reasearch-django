# from typing import Any
from urllib.request import Request
# from django import http
from django.shortcuts import render
from django.views import View
# from django.views.generic import ListView
# from django.views.generic import FormView
# from typing import Any
# from django.db import models
# from django.db.models.query import QuerySet
# from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
# from.models import Car
# from .form import CarCreateForm, UpdateCarForm
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.utils.text import slugify
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MySkillModel
from .form import Serachforms
# from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.db.models import Q


class HomeView(View):
    form_class = Serachforms
#     # http_method_names = ['post']
    templated_name = 'home/home.html'
    def get(self, request: Request):
        all_skills = MySkillModel.objects.all()
        form = self.form_class(request.GET)
        if form.is_valid():
            cd = form.cleaned_data.get('search')
            all_skills = MySkillModel.objects.filter(Q(name__icontains=cd) | Q(create_at__icontains=cd))
        context = {
            'all_skills': all_skills,
            'search_form': self.form_class,
        }
        return render(request, self.templated_name, context)

    # def get(self, request: Request):
    #     return render(request, self.templated_name)

    # def options(self, request, *args: Any, **kwargs: Any):
    #     responce =  super().options(request, *args, **kwargs)
    #     responce.headers['host'] = 'localhost'
    #     responce.headers['user'] = request.user
    #     return responce
    
    
    # def post(self, request, *args, **kwargs):
    #     pass
    
    # def http_method_not_allowed(self, request, *args: Any, **kwargs: Any):
        # super().http_method_not_allowed(request, *args, **kwargs)
        # return render(request, 'home/method_not-allowed.html')
        
        
# class HomeCarView(TemplateView):
#     template_name = 'home/home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cars'] = Car.objects.all()
#         return context


# class TwoView(RedirectView):
#     # url = 'https://www.google.com'
#     # url = '/%(id)i/%(car)s/'
    # pattern_name = 'homes:home'
#     # query_string = True
    
    # def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
#         print('=' * 90)
#         # print('processing url request')
        # print(kwargs['id'], print(kwargs['car']))
        # kwargs.pop('id')
        # kwargs.pop('car')
        # return super().get_redirect_url(*args, **kwargs)
    
    
# class HomeListView(ListView):
#     template_name = 'home/home.html'
#     model = Car
    # queryset = Car.objects.all()
    # queryset = Car.objects.filter(year__gte=2000)
    # context_object_name = 'cars'
    # ordering = ('-year', )
    # allow_empty = False
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     result = Car.objects.filter(year__gte=2000)
    #     return result
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context =  super().get_context_data(**kwargs)
    #     context['usernames'] = 'mohamamd'
    #     return context
    

# class HomeDetailView(LoginRequiredMixin, DetailView):
    # template_name = 'home/details-home.html'
    # model = Car
    # context_object_name = 'car'
    # slug_field = 'name'
    # pk_url_kwarg = 'integers'
    # queryset = Car.objects.all()
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return super().get_queryset()
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     if self.request.user.is_authenticated:
    #         return Car.objects.all()
    #     return Car.objects.none()
    
    # def get_object(self, queryset=None):
    #     return Car.objects.get(pk=self.kwargs['pk'],
    #                            name=self.kwargs['name'],
    #                            owner=self.kwargs['owner'],
    #                            slug=self.kwargs['slug'])
        
           
# class CreateCarView(FormView):
#     template_name = 'home/create-car.html'
#     form_class = CarCreateForm
#     # success_url = 'home/home.html'
#     success_url = reverse_lazy('homes:home')
    
#     def form_valid(self, form):
#         self._create_car(form.cleaned_data)
#         messages.success(self.request, 'create car successfully', 'success')
#         return super().form_valid(form)
    
    
#     def _create_car(self, data):
#         Car.objects.create(
#             name = data['name'],
#             year = data['year'],
#             owner = data['owner'],
#             slug = slugify(data['name'])
#         )
        

# class CreatePersionView(CreateView):
#     model = Person
#     fields = '__all__'
#     template_name = 'home/create-person.html'
#     success_url = reverse_lazy('homes:home')
        
        

# class CarCreateView(LoginRequiredMixin, CreateView):
#     model = Car
#     fields = ('name', 'year')
#     template_name = 'home/create-car.html'
#     success_url = reverse_lazy('homes:home')
    
    
#     def form_valid(self, form):
#         car = form.save(commit=False)
#         car.owner = self.request.user.username if self.request.user.username else 'anonymous user' 
#         car.slug = slugify(car.name)
#         car.save()
#         return super().form_valid(form)
    
    

# class DeleteCarView(LoginRequiredMixin, DeleteView):
#     model = Car
#     template_name = 'home/delete-car.html'
#     success_url = reverse_lazy('homes:home')
    
    
#     def form_valid(self, form):
#         messages.success(self.request, 'delete car successfully', 'success')
#         return super().form_valid(form)

    
# class UpdateCarView(LoginRequiredMixin, UpdateView):
#     model = Car
#     fields = ('name', 'year')
#     template_name = 'home/update-car.html'
    # success_url = reverse_lazy('homes:details_car')
    
    # def get_success_url(self):
    #     car = self.object
    #     return reverse_lazy("homes:details_car", args=[car.pk, car.name, car.owner, car.year, car.slug])
    
    # def form_valid(self, form):
    #     car = form.save(commit=False)
    #     car.slug = slugify(car.name)
    #     car.owner = self.request.user.username
    #     car.save()
    #     messages.success(self.request, 'update car successfully','success')
    #     return super().form_valid(form)
    
