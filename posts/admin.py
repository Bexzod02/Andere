from django.contrib import admin

from .models import Category, Post, Comment,Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at')
    list_filter = ['created_at', 'id']
    search_fields = ('title', 'category')
    #readonly_fields = ['created_at']
    prepopulated_fields = ({'slug': ('title', )})
    filter_horizontal = ('tags', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_filter = ['created_at']
    readonly_fields = list_filter
    search_fields = ('name', 'email')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
