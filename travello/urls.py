from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('destinations', views.destinations, name='destinations')
]
