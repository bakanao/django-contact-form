from django.shortcuts import render
from django.views.generic import TemplateView

from contact.models import Contact


class ContactView(TemplateView):
    template_name='contact.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name
        )

        return render(request, self.template_name, {})
