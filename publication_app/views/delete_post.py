from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect
from publication_app.models import Post

@login_required()
def delete_post(request, pk):

    Post.objects.get(id=pk).delete()
    return redirect('account')