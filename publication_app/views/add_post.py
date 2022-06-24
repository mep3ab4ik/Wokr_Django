from django.views import View
from django.shortcuts import render, redirect

from publication_app.models import Post, ImagePost
from publication_app.forms.add_post import ImagePostForm


class AddPost(View):
    """View добавление постов"""
    @staticmethod
    def get(request):
        form = ImagePostForm()

        context = {
            'title': 'Добавление нового поста',
            'form': form
        }

        return render(request, 'publication_app/add_post.html', context)

    @staticmethod
    def post(request):

        form = ImagePostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        tags = request.POST.getlist('tag')

        if len(files) > 4:
            context = {
                "title": "Добавление нового поста",
                "form": form,
                "error": "Максимальное количество фотографии - 4. Попробуйте снова"
            }
            return render(request, "publication_app/add_post.html", context)

        if form.is_valid():
            post_obj = Post.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                is_public=form.cleaned_data['is_public'],
            )

            for file in files:
                ImagePost.objects.create(
                    post=post_obj,
                    image=file
                )

            for tag in tags:
                post_obj.tag.add(tag)

            return redirect('posts')

        else:
            context = {
                'title': 'Добавление нового поста',
                'form': form
            }
            return render(request, 'publication_app/add_post.html', context)

