from django.views.generic import UpdateView
from publication_app.models import Post


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'text', 'is_public', 'imagine']

