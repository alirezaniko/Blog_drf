from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'comments', views.CommentViewSet)

app_name = "blog"
urlpatterns = [

    path('detail/<slug:slug>', views.article_details, name="article_detail"),
    path('list', views.articles_list, name="article_list"),
    path('category/<int:pk>',views.category_detail,name="category_detail"),
    path('search/',views.search,name="search_articles"),
    path('', include(router.urls)),

]
