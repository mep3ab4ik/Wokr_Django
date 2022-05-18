from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.decorators import login_required

from publication_app.views.site import Account
from publication_app.views.add_post import AddPost
from publication_app.views.edit_post import EditImagePost
from publication_app.views.delete_post import delete_post
from publication_app.views.get_tag import get_tag

urlpatterns = [
    path('site/', Account.as_view(), name='site'),
    path('add_post/', login_required(AddPost.as_view()), name='add_post'),
    path('edit_post/<int:pk>/', login_required(EditImagePost.as_view()), name='edit_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('tags/<str:tag>/', get_tag, name='get_tag')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()