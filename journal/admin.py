from django.contrib import admin
from models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'pub_date', 'category', 'body',
    'hero_image', 'optional_image')

admin.site.register(Article, ArticleAdmin)
