from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from publication_app.models import Post, ImagePost
from publication_app.forms.add_post import ImagePostForm


@login_required()
def add_post(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('image')
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            is_public = form.cleaned_data['is_public']
            post_obj = Post.objects.create(
                user=user,
                title=title,
                text=text,
                is_public=is_public
            )
            for f in files:
                ImagePost.objects.create(
                    post=post_obj,
                    image=f
                )
            return redirect('account')
    else:
        form = ImagePostForm()
        context = {
            'title': 'Добавление нового поста',
            'form': form
        }
    return render(request, 'add_post.html', context)