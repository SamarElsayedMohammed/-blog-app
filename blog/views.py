from django.shortcuts import render
from django.views.generic import ListView ,DetailView 
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name ='post/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name ='post/post_detail.html'


