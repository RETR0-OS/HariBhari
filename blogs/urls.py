from django.contrib import admin
from django.urls import path, include
from .views import blogs_getting_Listview, blogs_getting_Detailview, add_blog_view, edit_blog_view, delete_blog_view, like_view, add_comment_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	#path('', views.blogs_getting, name='blogs/'),
	path('', blogs_getting_Listview.as_view(), name='blogs/'),
	path('blog/<int:pk>', blogs_getting_Detailview.as_view(), name='blog-full'),
	path('new_blog/', add_blog_view.as_view(), name='add_blog'),
	path('update_blog/<int:pk>', edit_blog_view.as_view(), name='update_blog' ),
	path('delete_blog/<int:pk>', delete_blog_view.as_view(), name='delete_blog' ),
	path('like/<int:pk>', like_view, name='like_blog' ),
	path('blog/<int:pk>/comment', add_comment_view.as_view(), name='add_comment')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
