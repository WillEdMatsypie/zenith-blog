from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Post Title',
            }),
            'subtitle': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Post Caption'}),
            'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Post Text...'})
         }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            }),
            'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Comment...'})
         }