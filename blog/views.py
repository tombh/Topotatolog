from blog.models import Post
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

def index(request):    
    return direct_to_template(
        request,
        'index.html', {
        'posts': Post.objects.all()[:5]
    })

def view_post(request, slug):    
    return direct_to_template(
        request,
        'view_post.html',
        {'post': get_object_or_404(Post, slug=slug)}
    )