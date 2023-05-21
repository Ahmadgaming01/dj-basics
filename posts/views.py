from django.shortcuts import render
from.models import post
from.forms import PostForm
# Create your views here.


def posts_List(request):
    data = post.objects.all ()
    return render(request, 'posts/posts.html',{'posts':data})



def post_detail(request ,post_id):
    data = post.objects.get(id=post_id)
    return render (request , 'posts/detail.html',{'post':data})
 

def new_post (request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = PostForm()
    form = PostForm()
    return render (request , 'posts/new.html', {'form':form})

def edit_post (request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = PostForm()
    form = PostForm()
    return render (request , 'posts/new.html', {'form':form})