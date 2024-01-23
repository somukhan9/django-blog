from django.db import models

from authapp.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    post_image = models.ImageField(
        upload_to="uploads/post", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="category")
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
