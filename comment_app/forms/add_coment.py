from django import forms

from comment_app.models import Comment


class AddCommentsForm(forms.ModelForm):
    """Форма добавление комментарии к постам"""
    class Meta:
        model = Comment
        fields = ["text", "post", "user"]
        widgets = {
            "post": forms.HiddenInput(),
            "user": forms.HiddenInput(),
        }