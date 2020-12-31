from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)