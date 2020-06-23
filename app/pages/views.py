from django.shortcuts import render
from django.views.generic import DetailView

from .models import Page

def home(request):
    return render(request, 'base.html')

class SinglePage(DetailView):
    model = Page
    template_name = 'pages/index.html'
    slug_field = 'slug'
    slug_url_kwarg = 'page_slug'
    context_object_name = 'page'