from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_dojo', views.add_dojo),
    path('add_ninja', views.add_ninja),
    path('delete_ninja', views.delete_ninja),
]
