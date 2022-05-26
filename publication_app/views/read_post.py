from django.views import View
from django.shortcuts import render, redirect

from publication_app.models import Post
from comment_app.forms.add_coment import AddCommentsForm


# Создать html для кноки открыть пост нормальный ( На будущее )
class ReadPostView(View):

    @staticmethod
    def get(request, pk):
        posts = Post.objects.get(pk=pk)
        form = AddCommentsForm()
        context = {
            'title': 'Пост',
            'name_text': 'Публикации',
            'posts': posts,
            'form': form,
        }
        return render(request, 'publication_app/read_post.html', context)

    @staticmethod
    def post(request, pk):
        new_request = request.POST.copy()
        new_request['user'] = request.user.pk
        new_request['post'] = pk
        print(new_request)
        form = AddCommentsForm(data=new_request)
        if form.is_valid:
            form.save()
            return redirect(f'/post/{pk}')