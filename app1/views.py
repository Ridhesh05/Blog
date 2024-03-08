from django.shortcuts import render,redirect, get_object_or_404
from .models import Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import PostForm


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-created_on")
    paginator = Paginator(posts,3)
    page=request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    context ={"posts":posts,"categories": categories}
    return render(request,"app1/index.html",context)
def details(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        # Increment the like count
        post.likes += 1
        post.save()
    context={"post":post}
    return render(request,'app1/details.html',context)
def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by("-created_on")
    paginator=Paginator(posts,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    context = {"posts": posts, "category": category, "categories": categories}
    return render(request, "app1/category_posts.html", context)

def search(request):
    query = request.GET.get('q')
    if query:
        # Filter posts based on search query in title or body
        posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        posts = Post.objects.all()
    return render(request, 'app1/index.html', {'posts': posts})

def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Increment the like count
    post.likes += 1
    post.save()
    
    return HttpResponseRedirect(reverse('details', args=[id]))
def dislike_post(request,id):
    post=get_object_or_404(Post,id=id)
    # Decrement the likes and redirect
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect(reverse('details', args=[id]))



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'app1/create_post.html', {'form': form})

        
def delete_post(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'app1/confirmation_template.html', {'post': post})        

