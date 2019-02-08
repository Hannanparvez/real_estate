from django.contrib import admin
from .models import Blog,Comment,Reply

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','blog_author','blog_type','blog_date',)
    list_display_links=('id','blog_author')
    search_fields=('blog_author',)
    list_per_page=25
admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','comment_author','comment_content',)
    list_display_links=('id','comment_author',)
    list_per_page=25
admin.site.register(Comment,CommentAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display=('id','reply_to','reply_by','reply_content')
    list_display_links=('id',)
    list_per_page=25
admin.site.register(Reply,ReplyAdmin)
# Register your models here.
