from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post

def index(request):
    return render(request, 'network/index.html', {'posts': Post.objects.all()})

# TODO: implement feed by subscriptions
def feed(request):
    return render(request, 'network/index.html', {'posts': Post.objects.all()})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['text'] and request.FILES['image']:
            post = Post()
            post.author = request.user
            post.title = request.POST['title']
            post.text = request.POST['text']
            post.image = request.FILES['image']
            post.save()
            return redirect('index')
        else:
            return render(request, 'network/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'network/create.html')

# TODO: implement user page
