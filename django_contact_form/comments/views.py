from django.shortcuts import render
from django.views.generic import TemplateView

from comments.forms import CommentsForm


class CommentsView(TemplateView):
    template_name='comments.html'

    def get(self, request):
        form = CommentsForm()
        return render(
            request,
            self.template_name,
            {
                'form' : form}
            )
