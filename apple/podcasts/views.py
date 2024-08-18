import requests
from django.views.generic import TemplateView


class PodcastSearchView(TemplateView):
    template_name = 'podcast/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')
        if query:
            url = f'https://itunes.apple.com/search?term={query}&media=podcast&limit=10'
            response = requests.get(url).json()
            context['response'] = response
        return context
