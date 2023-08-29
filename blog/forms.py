# blog/forms.py
from django import forms
from rest_framework import serializers, viewsets
from .models import Post, Comment, HashTag

# Form: html에 있는 form 태그
# Model Form: model을 사용하는 form
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','category', 'content','target_number']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': '3', 'cols':'35'})
        }


class HashTagForm(forms.ModelForm):
    
    class Meta:
        model = HashTag
        fields = ['name']