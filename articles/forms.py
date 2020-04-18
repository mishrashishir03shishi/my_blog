from django.forms import ModelForm
from django import forms
from articles.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['content',]
		widgets = {
            'content': forms.TextInput(attrs={'placeholder':'Max 300 words...'})
        }