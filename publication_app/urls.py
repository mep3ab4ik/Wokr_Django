from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views.posts import Account
from .views.add_post import AddPost
from .views.edit_post import EditImagePost
from .views.delete_post import delete_post
from .views.get_tag import GetTag
from .views.read_post import ReadPostView
from .views.area_tag import Tags
from .api.views.publications import PostView, HashtagView, TagPostView, HashtagPostView

from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'posts', PostView)


urlpatterns = [
    path('posts/', Account.as_view(), name='posts'),
    path('add_post/', login_required(AddPost.as_view()), name='add_post'),
    path('edit_post/<int:pk>/', login_required(EditImagePost.as_view()), name='edit_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('post/<int:pk>', ReadPostView.as_view(), name='read_post'),
    path('tag/<str:tag>/', GetTag.as_view(), name='get_tag'),
    path('tags/', Tags.as_view(), name='tags'),
    path('api/', include(routers.urls)),
    # path('api/posts', PostView.as_view({'get': 'list', 'post': 'create'}), name='api-posts'),
    path('api/hashtag', HashtagView.as_view({'get': 'list'}), name='api-tags'),
    path('api/posttag/<str:tag>', TagPostView.as_view(), name='post-tag'),
    path('api/hashtag/<str:hashtag>', HashtagPostView.as_view(), name='hashtag-post'),




]
