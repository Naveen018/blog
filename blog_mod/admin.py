from django.contrib import admin

from blog_mod.models import Category, Blog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
