from django.contrib import admin
from BloggingApp.models import AddPost1

# Register your models here.

class AddPost1Admin(admin.ModelAdmin):
    list_display = ['Name', 'email', 'Write_Post']

admin.site.register(AddPost1, AddPost1Admin)


