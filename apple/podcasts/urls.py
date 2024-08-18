from django.urls import path
from .views import PodcastSearchView, PodcastEpisodesView


urlpatterns = [
    path('search/', PodcastSearchView.as_view(), name='search-podcasts'),
    path('<int:collection_id>/', PodcastEpisodesView.as_view(), name='episodes'),
]
