from django.views import View
from django.forms import modelformset_factory
from publication_app.forms.editpostform import EditPostForm
from django.shortcuts import render, redirect
from publication_app.models import Post, ImagePost


class EditImagePost(View):
    ImageFormSet = modelformset_factory(ImagePost, fields={"image", })

    def get(self, request, pk):
        get_post = Post.objects.get(pk=pk)

        post_form = EditPostForm(instance=get_post)
        image_form = self.ImageFormSet(queryset=ImagePost.objects.filter(post=get_post))
        context = {
            "title": "Добавить пост",
            "form": post_form,
            "image": image_form
        }
        return render(request, 'publication_app/edit_post.html', context)

    def post(self, request, pk):
        get_post = Post.objects.get(pk=pk)

        post_form = EditPostForm(data=request.POST, instance=get_post)

        form_image = self.ImageFormSet(request.POST or None, request.FILES or None)
        get_image = ImagePost.objects.filter(post=get_post)
        if post_form.is_valid() and form_image.is_valid():
            post_form.save()
            for i, file in enumerate(form_image):
                if file.cleaned_data:
                    if file.cleaned_data["id"] is None:
                        ImagePost(post=get_post, image=file.cleaned_data.get('image')).save()
                    elif file.cleaned_data["image"] is False:
                        ImagePost.objects.get(id=request.POST.get(f'form-{i}-id')).delete()
                    else:
                        image = ImagePost(post=get_post, image=file.cleaned_data.get('image'))
                        obj_img = ImagePost.objects.get(id=get_image[i].id)
                        obj_img.image = image.image
                        obj_img.save()
            return redirect('posts')
