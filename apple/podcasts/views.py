import json
import requests
from django.views.generic import TemplateView


class PodcastSearchView(TemplateView):
    template_name = 'podcasts/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')
        if query:
            url = f'https://itunes.apple.com/search?term={query}&media=podcast&limit=10'
            response = requests.get(url).json()
            context['response'] = response
        return context


class PodcastEpisodesView(TemplateView):
    template_name = 'podcasts/episodes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection_id = kwargs.get('collection_id')
        query = self.request.GET.get('query', '')
        url = f'https://itunes.apple.com/lookup?id={collection_id}&media=podcast&entity=podcastEpisode&limit=100'
        response = requests.get(url)
        episodes = response.json().get('results', [])
        if query:
            filtered_episodes = [
                episode for episode in episodes if query.lower() in episode.get('trackName', '').lower()]
            context['episodes'] = filtered_episodes
        else:
            context['episodes'] = episodes
        context['collection_id'] = collection_id
        return context

