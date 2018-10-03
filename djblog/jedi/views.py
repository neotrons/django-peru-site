from django.shortcuts import render
from django.views.generic import TemplateView
from jedi.models import SlideImage
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['jedi'] = {
            "sliders": SlideImage.objects.filter(active=True)
        }
        return context
