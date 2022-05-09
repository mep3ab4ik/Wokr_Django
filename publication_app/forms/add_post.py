from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(label='Заголовок поста', max_length=256)
    text = forms.CharField(label='Текст к посту')
    imagine = forms.ImageField(label='Выберите фото',  required=False)
    is_public = forms.BooleanField(label='Публичная запись', initial=True)
