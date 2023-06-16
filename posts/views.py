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


def new_post (request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/blog/')

    else:
        form = PostForm()
    
    return render (request , 'posts/new.html', {'form':form})

def edit_post (request ,post_id):
    data = post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES , instance=data)
        if form.is_valid():
            form.save()
            return redirect ('/blog/')

    else:
        form = PostForm(instance=data)
    
    return render (request , 'posts/edit.html', {'form':form})

def delete_post (request , post_id):
    data = post.objects.get(id=post_id)
    data.delete()
    return  redirect ('/blog/')
