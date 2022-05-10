from django import forms
from publication_app.models import Post


class EditPostForm(forms.ModelForm):
    """Класс формы для добавления постов"""
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', 'imagine']
#     title = forms.CharField(label='Редактирование заголовка', max_length=256)
#     text = forms.CharField(label='Редактирование тест')
#     # Параметр requered=False означает, что поле может быть пустым
#     imagine = forms.ImageField(label='Изменить фото',  required=False)
#     # Параметр initial=True ставил сразу галочку
#     is_public = forms.BooleanField(label='Публичная запись', initial=True)