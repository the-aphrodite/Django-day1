from django.urls import path
from . import views

urlpatterns = [
    path('trainee/', views.trainee_list, name='trainee_list'),
    path('trainee/add/', views.add_trainee, name='add_trainee'),
    path('trainee/update/<int:pk>/', views.update_trainee, name='update_trainee'),
    path('trainee/delete/<int:pk>/', views.delete_trainee, name='delete_trainee'),
]
