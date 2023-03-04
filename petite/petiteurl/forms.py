# listings/forms.py
from django import forms


class IndexPage(forms.Form):
    url = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control p-2",
               "id": "url",
               "placeholder": "Enter here the URL you want to shorten"
               }))

    expires_option = forms.BooleanField(required=False,
                                        label='Do you want the link to expire?',
                                        widget=forms.CheckboxInput(
                                            attrs={"id": "expires_opt"}))

    expiration = forms.DateTimeField(required=False, label="When? ",
                                     widget=forms.DateTimeInput(attrs={"type": "datetime-local",
                                                                       'class': "form-control p-1",
                                                                       "style": "width:200px;",
                                                                       "id": "expiration"}))

    custom_hash_option = forms.BooleanField(required=False, label="Do you want to personalized the hash value?",
                                            widget=forms.CheckboxInput(
                                                attrs={"id": "custom_opt"})
                                            )

    custom = forms.CharField(required=False, label="Enter personalized hash (8 characters long): ",
                             widget=forms.TextInput(attrs={"class": "form-control p-1",
                                                           "maxlength": "8",
                                                           "style": "width:200px;",
                                                           "id": "custom",
                                                           "minlength": "8"}))
