from django.urls import path
from . import views

urlpatterns = [
    path('traineelist/', views.trainee_list, name='trainee_list'),
    path('addtrainee/', views.add_trainee, name='add_trainee'),
    path('updatetrainee/<int:pk>/', views.update_trainee, name='update_trainee'),
    path('deletetrainee/<int:pk>/', views.delete_trainee, name='delete_trainee'),
]
