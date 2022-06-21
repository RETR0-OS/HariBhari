from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_head', 'blog_content', 'blog_summary', 'author', 'blog_header_image']

        widgets = {
            'blog_head' : forms.TextInput(attrs={'class': 'form-control'}),
            'blog_content' : forms.Textarea(attrs={'class': 'form-control'}),
            'blog_summary' : forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'author_username', 'required': 'required', 'type': 'hidden'}),
        }


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_head', 'blog_content', 'blog_summary']

        widgets = {
            'blog_head' : forms.TextInput(attrs={'class': 'form-control'}),
            'blog_content' : forms.Textarea(attrs={'class': 'form-control'}),
            'blog_summary' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
