from django.contrib import admin
from .models import Article, Category, Tag


# class TagInline(admin.TabularInline):


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category',
                    'author', 'pub_date', 'status', 'views']
    fieldsets = [
        (None, {'fields': ['title', 'content']}),
        ('选项', {'fields': [('status', 'category', 'author', 'tags')]}),
        ('其他', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    search_fields = ('title',)
    date_hierarchy = ('pub_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
