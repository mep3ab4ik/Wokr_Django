from django import forms
from publication_app.models import Post
from tag_app.models import Tag
import re
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    title = forms.CharField(label='Введите название поста')
    text = forms.CharField(
        label='Введите тест к посту',
        widget=forms.Textarea()
    )
    is_public = forms.BooleanField(
        label='Публичная запись ?',
        initial=True,
        required=False
    )

    tag = forms.ModelMultipleChoiceField(
        label='Тэги',
        required=False,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', 'tag']

    # Кастомный валидатор
    def clean_title(self):
        """Функция проверки поля 'title'

        Если 'title' начинается с цифры, выдаем ошибку с тексом,
        если нет, то возращаем 'title'
        """
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название поста не должно начинаться с цифры ')
        return title


class ImagePostForm(AddPostForm):
    image = forms.ImageField(
        label='Выберите фотографии',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(AddPostForm.Meta):
        fields = AddPostForm.Meta.fields + ['image', ]

