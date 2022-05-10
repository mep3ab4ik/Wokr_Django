from django import forms


class AddPostForm(forms.Form):
    """Класс формы для добавления постов"""
    title = forms.CharField(label='Заголовок поста', max_length=256)
    text = forms.CharField(label='Текст к посту')
    # Параметр requered=False означает, что поле может быть пустым
    imagine = forms.ImageField(label='Выберите фото',  required=False)
    # Параметр initial=True ставил сразу галочку
    is_public = forms.BooleanField(label='Публичная запись', initial=True,  required=False)
