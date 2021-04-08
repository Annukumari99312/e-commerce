from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Blogview(TemplateView):
    template_name = 'blog.html'
