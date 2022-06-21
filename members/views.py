from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import registerForm, editUserForm, CreateProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from blogs.models import Profile
# Create your views here.

class passwords_change_view(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_updated')

class user_register_view(generic.CreateView):
    form_class = registerForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class user_edit_view(generic.UpdateView):
    form_class = editUserForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class show_profile_page_view(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(show_profile_page_view, self).get_context_data()
        user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = user
        return context

def password_updated(request):
    return render(request, "registration/password_changed.html", {})

class edit_profile_page_view(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ['user_bio', 'user_avatar']
    success_url = reverse_lazy('home')

class create_profile_page(generic.CreateView):
    model = Profile
    template_name = "registration/create_user_profile_page.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
