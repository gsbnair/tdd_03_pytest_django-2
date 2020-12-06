# forms.py

from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ("description",)

    def clean_description(self):
        data = self.cleaned_data.get("description")
        if len(data) <= 5:
            raise forms.ValidationError("description is too short")
        return data
