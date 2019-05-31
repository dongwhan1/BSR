from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.homepage, name='homepage'),
]