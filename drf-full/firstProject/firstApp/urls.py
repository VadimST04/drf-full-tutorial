from django.urls import path

from firstApp import views

urlpatterns = [
    path('emps/', views.employee_view),
]
