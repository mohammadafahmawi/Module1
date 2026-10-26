from django.contrib import admin

from .models import Comment, User, Category, Post


#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'title', 'author')
    list_filter = ('title_id', 'title', 'author')
    search_fields = ('title_id', 'title', 'author')
    ordering = ('title_id', 'title', 'author')

#@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'password')

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)




