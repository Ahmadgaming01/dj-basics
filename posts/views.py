from django.shortcuts import render ,redirect
from.models import post
from.forms import PostForm
from django.views import generic
# Create your views here.


class PostList(generic.ListView):
    model = post
    

class PostDetail(generic.DetailView):
    model = post

class PostCreate(generic.CreateView):
    model=post
    fields = ['title', 'publish_date','content','author','image','tags']
    success_url = 'blog/'

class PostEdit(generic.UpdateView):
    model=post
    fields = ['title', 'publish_date','content','author','image','tags']
    success_url = 'blog/'
    template_name = 'posts/edit.html'


class PostDelete(generic.DeleteView):
    model = post
    success_url='blog/'

