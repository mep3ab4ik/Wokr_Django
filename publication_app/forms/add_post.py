from django import forms
from publication_app.models import Post
from tag_app.models import Tag


class AddPostForm(forms.ModelForm):
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

    tag = forms.ModelMultipleChoiceField(
        label='Тэги',
        required=False,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', 'tag']


class ImagePostForm(AddPostForm):
    image = forms.ImageField(
        label='Выберите фотографии',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(AddPostForm.Meta):
        fields = AddPostForm.Meta.fields + ['image', ]

