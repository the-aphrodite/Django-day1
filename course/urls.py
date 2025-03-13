from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_list, name='course_list'),
    path('course/add/', views.add_course, name='add_course'),
    path('course/update/<int:pk>/', views.update_course, name='update_course'),
    path('course/delete/<int:pk>/', views.delete_course, name='delete_course'),
]
