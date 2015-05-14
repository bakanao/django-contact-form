from django import forms


class CommentsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    comment = forms.CharField(widget = forms.Textarea)
    ip = forms.CharField(max_length=100, required=True)
