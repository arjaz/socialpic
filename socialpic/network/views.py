from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'network/index.html', {'posts': Post.objects.all()})
