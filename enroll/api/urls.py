from django.urls import path, include
from enroll.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
