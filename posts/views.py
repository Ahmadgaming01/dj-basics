from django.shortcuts import render
from.models import post
# Create your views here.


def posts_List(request):
    data = post.objects.all ()
    return render(request, 'posts/posts.html',{'posts':data})



def post_detail(request ,post_id):
    data = post.objects.get (id=post_id)
    return render (request , 'posts/post_detail.html',{'post':data})
