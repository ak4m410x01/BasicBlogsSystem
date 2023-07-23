from django.shortcuts import render
from .models import Post

# Create your views here.

from django.http import HttpResponse


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "post/post_list.html", {"all_posts": all_posts})
    # return HttpResponse("HEl")
