from django.contrib import admin
from .models import Article, Comment


# admin.site.register(Article)
# admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
     list_display = ('id', 'author', 'title', 'created_date',
        'published_date')
