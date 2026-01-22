from django.urls import path
from .views import search_voter

urlpatterns = [
    path('search/', search_voter),
]