from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from . models import Post
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.
#def main(request):
    #return render(request , 'main.html' , {})

class Home(ListView):
    model = Post
    template_name = "main.html"
    ordering = ["-id"]

class Detail(DetailView):
    model = Post
    template_name = "detail.html"

class AddPost(CreateView):
    model = Post
    template_name = "addpost.html" 
    fields = "__all__"

class UpdatePost(UpdateView):
    model = Post
    template_name = "updatepost.html"
    fields = ['title' , 'body' , 'author']

class DeletePost(DeleteView , SuccessMessageMixin):
    model=Post
    template_name = "deletepost.html"
    success_url = reverse_lazy('main')

