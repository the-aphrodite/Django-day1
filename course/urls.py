from django.urls import path
from . import views

urlpatterns = [
    path('courselist/', views.course_list, name='course_list'),
    path('addcourse/', views.add_course, name='add_course'),
    path('updatecourse/<int:pk>/', views.update_course, name='update_course'),
    path('deletecourse/<int:pk>/', views.delete_course, name='delete_course'),
]
