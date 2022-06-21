from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, Comment
from .forms import BlogForm, EditBlogForm, CommentsForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
# Create your views here.

class blogs_getting_Listview(ListView):
    model = Blog
    template_name =  'blogs.html'
    ordering = ["-blog_date"]
    '''def get_context_data(self, *args, **kwargs):
        context = super(blogs_getting_Listview, self).get_context_data()
        authors_id_list = Blog.objects.all().values_list("author")
        authors_list = ""
        for author in authors_id_list:
            author_obj = User.objects.get(id=author)
            authors_list = authors_list + author_obj
        context.update({
            "authors_list": authors_list
            #'more_context': Model.objects.all(),
        })
        print(type(context["authors_list"]))
        return context'''

class blogs_getting_Detailview(DetailView):
    model = Blog
    template_name = 'blog_full.html'
    form_class = CommentsForm
    def get_context_data(self, *args, **kwargs):
        context = super(blogs_getting_Detailview, self).get_context_data()
        variable = get_object_or_404(Blog, id=self.kwargs['pk'])
        liked = False
        if variable.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_likes = variable.blog_likes_count()
        context["number_of_likes"] = total_likes
        context["liked"] = liked
        return context

class add_blog_view(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "add_blog.html"
    #fields = '__all__'

class edit_blog_view(UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'update_blog.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    #fields = ['blog_head', 'blog_content', 'blog_summary']

class delete_blog_view(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blogs/')

def like_view(request, pk):
    blog = get_object_or_404(Blog, id=request.POST.get('like_blog_id'))
    liked = False
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        liked = False
    else:
        blog.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse("blog-full", args=[str(pk)]))

'''def comment_view(request, pk):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            user_comment = form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/blogs/blog/%s' %post.id)

    else:
        return HttpResponseRedirect('/blogs' %post.id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)'''


class add_comment_view(CreateView):
    model = Comment
    form_class = CommentsForm
    template_name = "add_comment.html"
    ordering = ["-date"]
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('blogs/')
