from django import forms

from images.models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Image
        fields = ["image"]
