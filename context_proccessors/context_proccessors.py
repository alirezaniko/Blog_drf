from blog_app.models import Article, Category


def recent_articles(request):
    recent_articles = Article.custom_manager.order_by('-created')[:3]
    return {"recent_articles": recent_articles}


def category(request):
    category = Category.objects.all()
    return {"category": category}
