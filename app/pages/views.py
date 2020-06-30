from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin, FormView, CreateView

from .models import Page, Feedback
from .forms import FeedBackForm


def get_home(request):
    return render(request, 'base.html')


def error_404(request, exception):
    return render(request, 'pages/404.html')


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

    def form_valid(self, form):
        form.save(commit=False)
        send_mail(subject=form.cleaned_data['subject'],
                  message=f"""
                    Почта: {form.cleaned_data['name']}, 
                    Email: {form.cleaned_data['email']}, 
                    Сообщение: {form.cleaned_data['content']}
                """,
                  from_email='info@kuskovan.ru',
                  recipient_list=['andreykusk@yandex.ru', 'info@kuskovan.ru'],
                  fail_silently=False)
        form.save()
        return super().form_valid(form)


    def get_success_message(self, cleaned_data):
        return 'Спасибо за письмо. В ближайшее время свяжусь с вами!'



