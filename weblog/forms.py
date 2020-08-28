from django import forms
from .models import Post, Comment

# Form to add comments to posts
class PostComment(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'content')