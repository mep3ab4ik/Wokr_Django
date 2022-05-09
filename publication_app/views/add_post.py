from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from publication_app.models import Post
from publication_app.forms.add_post import AddPostForm


@login_required()
def add_post(request):
    """Функция для добавления постов"""
    if request.method == 'POST':
        form = AddPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_request = form.cleaned_data
            # Создаем new_request и в поля 'user_id' добавляем pk(можно id). Без этого error
            new_request['user_id'] = request.user.pk
            Post.objects.create(**new_request)
            return redirect('account')
    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {'form': form})