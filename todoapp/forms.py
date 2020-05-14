from django import forms
from django.utils import timezone

class Todo_forms(forms.Form):

    text = forms.CharField(label='', widget=forms.TextInput(
                                                        attrs={
                                                            "placeholder": "type here..."
                                                        }
                                                    )
                                                )

