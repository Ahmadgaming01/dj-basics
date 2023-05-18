from django import forms
from.models import post


class PostForm (forms.ModelForm):
    class meta :
        model = post
        fields = '__all__'
