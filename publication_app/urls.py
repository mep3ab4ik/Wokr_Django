from django.urls import path
from django.contrib.auth.decorators import login_required

from .views.posts import Account
from .views.add_post import AddPost
from .views.edit_post import EditImagePost
from .views.delete_post import delete_post
from .views.get_tag import GetTag
from .views.read_post import ReadPostView


urlpatterns = [
    path('posts/', Account.as_view(), name='posts'),
    path('add_post/', login_required(AddPost.as_view()), name='add_post'),
    path('edit_post/<int:pk>/', login_required(EditImagePost.as_view()), name='edit_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('post/<int:pk>', ReadPostView.as_view(), name='read_post'),
    path('tags/<str:tag>/', GetTag.as_view(), name='get_tag'),
]
