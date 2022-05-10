from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from publication_app.forms.EditPostForm import EditPostForm
from publication_app.models import Post


@login_required()
def edit_post(request, pk):
    """Функция редактирования пользователя"""
    # post EditPostForm(get=pk)
    # if request.method == 'POST':
    #     print(request.POST)
    #     # параметр 'instance' заполняет поля, если в бд есть данные
    #     post_form = EditPostForm(data=request.POST, files=request.FILES)
    #     if post_form.is_valid():
    #         post_form.save()
    #         return redirect('account')
    # else:
    #     post_form = EditPostForm()
    #     return render(request,
    #                   'edit_post.html',
    #                   {'post_form': post_form})

    posts = Post.objects.get(id=pk)

    if request.method == "POST":
        posts.title = request.POST.get("title")
        posts.text = request.POST.get("text")
        # posts.is_public = request.POST.get("is_public")
        posts.imagine = request.POST.get("imagine")
        posts.save()
        return redirect("account")
    else:
        return render(request, "edit_post.html", {"posts": posts})
