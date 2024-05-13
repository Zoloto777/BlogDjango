from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import CommentForm
from .models import Blog, Post, Comment, Blogger

def home(request):
    return render(request, 'blog/home.html')



class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = context['blogs']
        for blog in blogs:
            blog.posts = blog.post_set.all()[:5]
        return context


class BloggerListView(ListView):
    model = Blogger
    template_name = 'blog/blogger_list.html'
    context_object_name = 'bloggers'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.author = request.user.username
            else:
                comment.author = "Anonymous"  # Устанавливаем автора, если пользователь не вошел в систему
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post_title': post.title})

def blogger_detail(request, blogger_id):
    blogger = get_object_or_404(Blogger, pk=blogger_id)
    posts = Post.objects.filter(author=blogger.user)
    return render(request, 'blog/blogger_detail.html', {'blogger': blogger, 'posts': posts})