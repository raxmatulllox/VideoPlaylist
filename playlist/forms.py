from django import forms
from .models import VideoModel


# create a ModelForm
class VideoModelForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = '__all__'
