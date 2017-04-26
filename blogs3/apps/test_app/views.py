from django.shortcuts import render, redirect
from .models import Blogs, Comment


# Create your views here.
def index(request):
    context = {
        "blogs": Blogs.objects.all()
    }
    return render(request, 'index.html', context)


def blogs(request):
    Blogs.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    return redirect('/')


def comment(request,id):
    blog = Blogs.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')
