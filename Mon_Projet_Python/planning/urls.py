from django.urls import path

from . import views

urlpatterns = [
    path('', views.planning, name='planning'),
]