from django.urls import path
from . import views


app_name = 'homes'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.HomeCarView.as_view(), name='home'),
    # path('two/<int:id>/<str:car>/', views.TwoView.as_view(), name='two'),
    # path('', views.HomeListView.as_view(), name='home'),
    # path('<int:pk>/<str:name>/<str:owner>/<int:year>/<slug:slug>/', views.HomeDetailView.as_view(), name='details_car'),
    # path('create-car/', views.CreateCarView.as_view(), name='create_car'),
    # path('create-person/', views.CreatePersionView.as_view(), name='create_person'),
    # path('create-car/', views.CarCreateView.as_view(), name='create_car'),
    # path('delete-car/<int:pk>/', views.DeleteCarView.as_view(), name='delete_car'),
    # path('update-car/<int:pk>/', views.UpdateCarView.as_view(), name='update_car'),
]
