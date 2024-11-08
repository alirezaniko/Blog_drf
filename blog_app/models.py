from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=20)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(published=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="انتخاب نویسنده", related_name="articles")
    title = models.CharField(max_length=70, help_text="موضوع مقاله را بنویسید", unique_for_date='pub_date')
    category = models.ManyToManyField(Category, related_name="article")
    body = models.TextField(help_text="متن مقاله را بنویسید", null=True)
    body_Description = models.TextField()
    image = models.ImageField(upload_to='images/article', help_text="تصویر مورد نظر را آپلود کنید")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now)
    myfile = models.FileField(upload_to="myfile")
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    objects = models.Manager()
    custom_manager = ArticleManager()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'stories'
        ordering = ('-created',)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolut_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - published status :{self.published}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.title} - {self.body[:50]}"
