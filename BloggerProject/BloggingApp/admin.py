from django.contrib import admin
from BloggingApp.models import AddPost1, Comment

# Register your models here.

class AddPost1Admin(admin.ModelAdmin):
    list_display = ['Name', 'email', 'Write_Post', 'image']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('Name',  'post', 'body', 'commented')
    list_filter = ( 'commented',)
    search_fields = ('Name',  'body')

admin.site.register(AddPost1, AddPost1Admin)
admin.site.register(Comment, CommentAdmin)

