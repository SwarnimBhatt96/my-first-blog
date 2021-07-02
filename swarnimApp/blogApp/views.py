from django.shortcuts import get_object_or_404, render, redirect

from django.utils import timezone


from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def postList(request):
    posts = Post.objects.filter(publishDate__lte  = timezone.now()).order_by('publishDate')
    return render(request, 'blog/postList.html', {'posts': posts})


def postDetails(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/postDetails.html', {'post': post})


@login_required
def postNew(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # commit=False means that we don't want to save the Post model yet – we want to add the author first
            
            post.author = request.user
            # post.createdDate = timezone.now() its default
            # post.publishDate = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
        
    else:
        form = PostForm()
        return render(request, 'blog/postEdit.html', {'form': form})

@login_required
def postEdit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        # we pass this post as an instance, both when we save the form…
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.publishDate = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
        
    else:
        form  = PostForm(instance = post)
    return render(request, 'blog/postEdit.html', {'form': form})
    
    
@login_required
def postDraftList(request):
    drafts = Post.objects.filter(publishDate__isnull = True).order_by('createdDate')
    return render(request, 'blog/postDraftList.html', {'drafts': drafts})

@login_required
def postPublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    
    return redirect('post_detail', pk = pk)

@login_required
def postDelete(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('post_list')


def addComment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk= post.pk)
        
    else:   
        form = CommentForm()
    return render(request, 'blog/addComment.html', {'form': form})
        
@login_required
def approveComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)
    
@login_required
def removeComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
    