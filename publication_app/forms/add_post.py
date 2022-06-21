from django import forms
from django.core.exceptions import ValidationError
import re

from publication_app.models import Post
from tag_app.models import Tag


class AddPostForm(forms.ModelForm):
    """Класс формы добавление поста"""
    title = forms.CharField(label='Введите название поста*')
    text = forms.CharField(
        label='Введите тест к посту*',
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
        если нет, то возвращаем 'title'
        """
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название поста не должно начинаться с цифры.')
        return title


class ImagePostForm(AddPostForm):
    """Класс формы добавление изображение к посту"""
    image = forms.ImageField(
        label='Выберите фотографии',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(AddPostForm.Meta):
        fields = AddPostForm.Meta.fields + ['image', ]

    # Валидатор на количество картинок
    def clean_image(self):
        image = self.cleaned_data['image']

        if len(image) > 4:
            raise ValidationError('Максимальное количество загружаемых фотографий не больше 4. Попробуйте снова. ')
        return image
