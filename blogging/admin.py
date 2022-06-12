from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class PostInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]
    include = "categories"


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Category, CategoryAdmin)
