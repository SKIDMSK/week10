from typing import Any
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, DetailView
from .models import News


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = News.objects.filter(is_published=True).order_by('-created')[:6]
        context['news_list'] = news_list
        return context

index = IndexView.as_view()

from django.views.generic import ListView
from .models import News

class NewsListView(ListView):

    template_name = 'news/list.html'
    model = News
    context_object_name = 'news_list'

news_list = NewsListView.as_view()

from django.views.generic import DetailView
from .models import News

class NewsDetailView(DetailView):

    template_name = 'news/detail.html'
    model = News
    context_object_name = 'news'

news_detail = NewsDetailView.as_view()

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contact

class ContactView(CreateView):

    template_name = 'contact.html'
    model = Contact
    fields = ('name', 'email', 'body')
    success_url = reverse_lazy('homepage:index')

    def form_valid(self, form):
        contact = form.save()
        print(contact.body)
        return super().form_valid(form)

contact = ContactView.as_view()