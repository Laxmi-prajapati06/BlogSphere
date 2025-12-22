from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden
from .models import Post, Category
from .forms import UserRegisterForm, PostForm

# Add this logout view
@require_http_methods(["GET", "POST"])
@login_required
def logout_view(request):
    if request.method == 'GET':
        # Show confirmation page
        return render(request, 'blog/logout_confirm.html')
    
    # POST request - perform logout
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')


def home(request):
    posts = Post.objects.all()[:6]
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """View a single post in detail"""
    post = get_object_or_404(Post, pk=pk)
    
    # Get related posts (same category, excluding current post)
    related_posts = Post.objects.filter(
        category=post.category
    ).exclude(id=post.id)[:3]
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'related_posts': related_posts
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})


@login_required
def create_post(request):
    # Get all categories for the template
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {
        'form': form,
        'categories': categories  # Pass categories to template
    })

@login_required
def create_post_simple(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        # Create post manually
        title = request.POST.get('title')
        excerpt = request.POST.get('excerpt', '')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')
        
        # Validate required fields
        if not title or not content:
            messages.error(request, 'Title and content are required')
            return render(request, 'blog/create_post_simple.html', {
                'categories': categories,
                'form_data': request.POST
            })
        
        # Create post
        post = Post(
            title=title,
            excerpt=excerpt,
            content=content,
            author=request.user,
            image=image
        )
        
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                post.category = category
            except Category.DoesNotExist:
                pass
        
        post.save()
        messages.success(request, 'Post created successfully!')
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'blog/create_post_simple.html', {
        'categories': categories
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden
from .models import Post, Category
from .forms import UserRegisterForm, PostForm

# ... your existing views ...

@login_required
def edit_post(request, pk):
    """Edit an existing post"""
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the current user is the author
    if post.author != request.user:
        return HttpResponseForbidden("You don't have permission to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    categories = Category.objects.all()
    return render(request, 'blog/edit_post.html', {
        'form': form,
        'post': post,
        'categories': categories,
        'title': 'Edit Post'
    })

@login_required
@require_http_methods(["POST"])
def delete_post(request, pk):
    """Delete a post"""
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the current user is the author
    if post.author != request.user:
        return HttpResponseForbidden("You don't have permission to delete this post.")
    
    # Delete the post
    post_title = post.title
    post.delete()
    
    messages.success(request, f'Post "{post_title}" has been deleted successfully!')
    return redirect('my_posts')