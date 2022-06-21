from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import user_register_view, user_edit_view, passwords_change_view, show_profile_page_view, edit_profile_page_view, create_profile_page
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', user_register_view.as_view(), name="register"),
    path('edit_account/', user_edit_view.as_view(), name="edit_account"),
    path('password/', passwords_change_view.as_view(template_name="registration/change_password.html"), name="change_password"),
    path('password_updated', views.password_updated, name="password_updated"),
    path('<int:pk>/profile', show_profile_page_view.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile_page', edit_profile_page_view.as_view(), name='edit_profile_page'),
    path('create_profile_page', create_profile_page.as_view(), name='create_profile_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
