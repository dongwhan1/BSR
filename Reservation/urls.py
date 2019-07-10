from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.homepage, name='homepage'),
    path(r'schedule', views.schedule, name='schedule'),
    path(r'makereserv', views.makereserv, name='makereserv'),
]