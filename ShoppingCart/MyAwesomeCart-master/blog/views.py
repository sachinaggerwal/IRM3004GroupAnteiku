'''
creating views
'''
# pylint: disable=redefined-builtin
from django.shortcuts import render
from .models import Blogpost

def index(request):
    '''
    creating posts
    '''
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html',
                  {'myposts': myposts})

def blogpost(request, id):
    '''
    viewing posts
    '''
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})
