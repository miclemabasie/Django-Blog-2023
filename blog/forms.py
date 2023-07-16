from django import forms
from .models import Post, Comment
from django import forms
from django_editorjs.widgets import EditorJsWidget


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            },
        )
    )


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "tags", "status")
