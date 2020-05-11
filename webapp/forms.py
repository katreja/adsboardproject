from django import forms

class IklanForm(forms.Form):
    name = forms.CharField(max_length=200)
    judul = forms.CharField(max_length=200)
    deskripsi = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=16)
    email = forms.EmailField(required=False)