from django.shortcuts import redirect

from publication_app.models import Post


# Функция удаления постов
def delete_post(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('posts')
