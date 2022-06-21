from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    blog_head = models.CharField(max_length=40)
    blog_header_image = models.ImageField(upload_to="photos/blogs/", null=True, blank=True)
    #blog_content = models.TextField()
    blog_content = RichTextField(blank=True, null=True)
    #blog_summary = models.TextField(max_length=355)
    blog_summary = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post_likes', blank=True)

    def __str__(self):
        return self.blog_head
    def get_absolute_url(self):
        return reverse('blog-full', args=[str(self.id)])
    def blog_likes_count(self):
        return self.likes.count()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_bio = models.TextField()
    user_avatar = models.ImageField(upload_to="photos/users/avatars/", null=True, blank=True)
    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s | %s' % (self.post.blog_head, self.name)
