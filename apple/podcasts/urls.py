from django.urls import path
from .views import PodcastSearchView


urlpatterns = [
    path('search/', PodcastSearchView.as_view(), name='search-podcasts'),
]
