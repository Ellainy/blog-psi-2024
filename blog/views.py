from django.shortcuts import render
from .models import Post


def index(request):
    return render(request,"index.html")

def sobre(request):
    return render(request,"aboutus.html")

def diturbios(request):
    posts = Post.objects.all()

    context = {
        "posts" : posts,
    }

    return render(request,"disturbs.html", context)

def ajuda(request):
    return render(request,"help.html")
