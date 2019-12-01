from django.contrib import admin
from comments.models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content_object','text','comment_time','user')


