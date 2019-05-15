from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
# this is our Controller

def index(request):
    # return HttpResponse('HELLO FROM POSTS')
    
    posts = Posts.objects.all()[:10] #get the first 10 posts
    
    context = {
            'title': 'Latest Posts from Views. DYNAMIC, BABY!!',
            'posts': posts,
            }
    
    return render(request, 'posts/index.html', context)

#fetch a single post
def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
            'post': post
            }
    
    return render(request, 'posts/details.html', context)