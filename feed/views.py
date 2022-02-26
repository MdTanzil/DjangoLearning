from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import Postform
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-id')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'


class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class = Postform
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        new_object = Post.objects.create(
            title=form.cleaned_data['title'],
            image=form.cleaned_data['image'],

        )
        messages.add_message(self.request, messages.SUCCESS,
                             'Post Upload successfully')

        return super().form_valid(form)
