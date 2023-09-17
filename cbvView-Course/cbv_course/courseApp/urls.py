from django.urls import path, include

from courseApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('courses/', views.CourseList.as_view()),
#     path('courses/<int:pk>/', views.CourseDetail.as_view()),
# ]