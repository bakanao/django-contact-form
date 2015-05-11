from django.shortcuts import render
from django.views.generic import TemplateView

from contact.models import Contact
from contact.forms import ContactForm

class ContactView(TemplateView):
    template_name='contact.html'

    def get(self, request):
        form = ContactForm()
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

    def post(self, request):
        form =ContactForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Contact.objects.create(
                first_name=cleaned_data['first_name'],
                last_name=cleaned_data['last_name']
            )

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )


class ThankYouView(TemplateView):
    template_name='thank.html'
