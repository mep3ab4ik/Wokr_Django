from django import forms
from publication_app.models import Post


class EditPostForm(forms.ModelForm):
    """Класс формы для добавления постов"""
    title = forms.CharField(label='Введите название поста')
    text = forms.CharField(
        label='Введите тест к посту',
        widget=forms.TextInput(attrs={'size': '80'})
    )
    is_public = forms.BooleanField(
        label='Публичная запись ?',
        initial=True,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public']