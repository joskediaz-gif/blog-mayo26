from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView

# Create your views here.
class BloglistView(ListView):
    model = Blog
    template_name = 'post-list.html'
