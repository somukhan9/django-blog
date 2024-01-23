from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Post


class HomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        latest_posts = Post.objects.all().order_by('-created_at')[:3]
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = latest_posts
        return context
