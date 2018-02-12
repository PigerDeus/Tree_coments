from django.shortcuts import render, redirect
from .models import Comment, SubComment
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        return render(request,
                  "index.html",
                  {})

def posts(request):
    if request.method == 'POST' and len(request.POST['message'])>0:
        if len(request.POST['parent_id'].split('c')) == 1:
            if request.POST['parent_id'] == '0':
                q = Comment(text = request.POST['message'], author = User.objects.get(username = request.user.username))
                q.save()
                return redirect('posts')
            else:
                q = SubComment(coment = Comment.objects.get(pk = request.POST['parent_id']),author = User.objects.get(username = request.user.username),text = request.POST['message'])
                q.save()
                return redirect('posts')
        else:
            index = request.POST['parent_id'].split('c')
            q = SubComment(coment = Comment.objects.get(
            pk = index[0]),
            parent = SubComment.objects.get(pk =index[1]),
            author = User.objects.get(username = request.user.username),
            text = request.POST['message'])
            q.save()
            return redirect('posts')

    comments = Comment.objects.all().order_by('-public_date')
    sub_coment = SubComment.objects.all().order_by('path')
    return render(request,
                  "posts.html",
                  {'coment':comments, 'sub_coment': sub_coment})

def comments(request):
    comments = Comment.objects.all()
    return render(request, "posts.html", {'comments': comments})
