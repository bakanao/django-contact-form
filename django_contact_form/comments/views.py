from django.shortcuts import render
from django.views.generic import TemplateView


class CommentsView(TemplateView):
    template_name='comments.html'
