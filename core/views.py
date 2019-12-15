# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'

    message = 'Hello World'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = self.message
        return context
