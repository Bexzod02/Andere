from django.shortcuts import render,redirect,get_object_or_404
from .models import Comment, Category, Tag, Post
from contact.models import Subscribe
from .forms import CommentForm
def hom_view(request):
    posts = Post.objects.order_by('-id')
    cates = request.GET.get('cates')
    last_2_articles = Post.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()    
    tag = request.GET.get('tag')
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
    if tag:
        posts = posts.filter(tags__tag__exact=tag)
    if cates:
        posts = posts.filter(category__title__exact=cates)
    context = {'object_list' : posts,'categories': categories,'tags': tags, 'last_2_articles': last_2_articles,}

    return render(request, 'posts/index.html', context)

def single_view(request, slug):
    form = CommentForm()
    article = get_object_or_404(Post, slug=slug)
    last_2_articles = Post.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(article__slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(f'/single/{article.slug}#comments')
    context = {
        #'object_list' : posts,
        'object': article,
        'last_2_articles': last_2_articles,
        'categories': categories,
        'tags': tags,
        'comments': comments,
        'form':form
    }

    return render(request, 'posts/single.html', context)

def fash_view(request):
    posts = Post.objects.order_by('-id')
    query = request.GET.get('query')
    if query:
        posts = posts.filter(title__icontains=query)
    context = {
        'object_list' : posts,
        'searchs':query,
    }

    return render(request, 'posts/fashion.html', context)

def travel_view(request):
    posts = Post.objects.order_by('-id')
    categories = Category.objects.all()
    last_2_articles = Post.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    context = {'object_list' : posts,'categories': categories,'tags': tags, 'last_2_articles': last_2_articles,}

    return render(request, 'posts/travel.html', context)

def about_view(request):
    posts = Post.objects.order_by('-id')

    context = {'object_list' : posts}

    return render(request, 'posts/about.html', context)



