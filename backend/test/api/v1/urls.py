from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Actual_workViewSet

router = DefaultRouter()
router.register("actual_work", Actual_workViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
