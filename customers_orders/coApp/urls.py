from django.urls import path, include
from rest_framework.routers import DefaultRouter

from coApp import views

router = DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]