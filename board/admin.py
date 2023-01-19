from django.contrib import admin
from .models import *

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_create', 'photo', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class CommentArticlesAdmin(admin.ModelAdmin):
    list_display = ('commentArticles', 'commentAuthor', 'text', 'dateCreation')
    list_display_links = ('commentArticles', 'commentAuthor')
    search_fields = ('commentArticles', 'commentAuthor', 'text', 'dateCreation')

admin.site.register(Author)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CommentArticles, CommentArticlesAdmin)






