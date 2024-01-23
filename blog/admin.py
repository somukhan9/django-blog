from django.contrib import admin

from .models import Tag, Category, Post

# Register your models here.


class PostConfig(admin.ModelAdmin):
    model = Post
    list_display = ("title", "author", "created_at")
    list_filter = ("author", "category", "created_at")
    prepopulated_fields = {
        "slug": ("title",)
    }


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, PostConfig)
