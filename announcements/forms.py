from django import forms
from models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }