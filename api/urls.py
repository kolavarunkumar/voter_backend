from django.urls import path
from .views import search_voter, test_db

urlpatterns = [
    path('search/', search_voter),
    path('test-db/', test_db),  # <-- temporary test
]
