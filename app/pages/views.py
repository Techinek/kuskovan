from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin, FormView, CreateView

from .models import Page, Feedback
from .forms import FeedBackForm

def get_home(request):
    return render(request, 'base.html')


class SinglePage(DetailView):
    model = Page
    template_name = 'pages/index.html'
    slug_field = 'slug'
    slug_url_kwarg = 'page_slug'
    context_object_name = 'page'


class ContactPage(SuccessMessageMixin,CreateView):
    template_name = 'pages/contacts.html'
    form_class = FeedBackForm
    success_url = reverse_lazy('contacts')

    def get_success_message(self, cleaned_data):
        return 'Спасибо за письмо. В ближайшее время свяжусь с вами!'


