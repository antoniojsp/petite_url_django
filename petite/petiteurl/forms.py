# listings/forms.py

from django import forms


class IndexPage(forms.Form):
    url = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control p-2",
               "id": "url",
               "placeholder": "Enter here the URL you want to shorten",
               "name": "url"}))

    expires_option = forms.BooleanField(label='Do you want the link to expire?', widget=forms.CheckboxInput(
        attrs={"id": "expires_opt",
               "name": "expires_opt"}))
    expiration = forms.DateTimeField(required=False)
    custom_hash_option = forms.BooleanField(label="Do you want to personalized the hash value?",
                                      )
    personalized = forms.CharField(required=False)
