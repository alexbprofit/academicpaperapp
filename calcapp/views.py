from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from .models import Post
from . import top


def post_new(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            posts.delete()
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'calcapp/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'calcapp/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    result = top.main(top.f,post.param1, post.param2, post.param3,post.nums,post.epsilon)
    # post.param1,post.param2 = top.main(top.f,post.param1, post.param2, post.param3,post.nums,post.epsilon)
    return render(request, 'calcapp/post_detail.html', {'post': post, 'result1': result[0], 'result2': result[1]})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'calcapp/post_list.html', {'posts': posts})
