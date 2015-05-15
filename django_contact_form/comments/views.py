from django.shortcuts import render
from django.views.generic import TemplateView

from comments.models import Comments
from comments.forms import CommentsForm

class CommentsView(TemplateView):
    template_name='comments.html'

    def get(self, request):
        form = CommentsForm()
        return render(
            request,
            self.template_name,
            {
                'form' : form
            }
        )

    def post(self, request):
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Comments.objects.create(
                name=cleaned_data['name'],
                comment=cleaned_data['comment']
            )
        return render(
            request,
            self.template_name,
            {}
       )
