from django.urls import path
from .views import operation


urlpatterns = [
    path('compute/', operation),
]
