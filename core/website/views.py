from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
#####
from blogs.models import Post

# Create your views here.

class IndexView(TemplateView):
    """
    a class based view to show index
    """
    template_name = 'website/index.html'

