from django.shortcuts import render, get_object_or_404
from blog_app.models import Article, Category, Comment
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Article, Comment
from .serializers import CategorySerializer, ArticleSerializer, CommentSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)

    return render(request, "blog/article_details.html", {'article': article})


def articles_list(request):
    article_list = Article.custom_manager.all()
    paginator = Paginator(article_list, 2)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    return render(request, "blog/articles_list.html", {'articles': object_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.article.all()
    return render(request, "blog/articles_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {'articles': object_list})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'body']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
