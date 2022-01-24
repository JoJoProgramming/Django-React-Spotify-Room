from django.urls import path
from .views import main
#import main class from the views.py file
urlpatterns = [
    path('home', main)
]