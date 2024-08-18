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
        if query:
            url = f'https://itunes.apple.com/lookup?id={collection_id}&entity=podcastEpisode&term={query}'
            response = requests.get(url)
            with open('response.json', 'w') as file:
                file.write(json.dumps(response.json(), indent=4))
            context['episodes'] = response.json().get('results', [])
            context['collection_id'] = collection_id
        return context

