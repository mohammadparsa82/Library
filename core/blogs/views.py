from django.shortcuts import render
from django.views.generic.base import TemplateView


from blogs.models import Post
# Create your views here.

class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context

