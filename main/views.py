from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView
from . models import Post
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
#def main(request):
    #return render(request , 'main.html' , {})

class Home(ListView):
    model = Post
    template_name = "main.html"

class Detail(DetailView):
    model = Post
    template_name = "detail.html"

class AddPost(CreateView):
    model = Post
    template_name = "addpost.html" 
    fields = "__all__"

class UpdatePost(SuccessMessageMixin , UpdateView):
    model = Post
    template_name = "updatepost.html"
    fields = ['title' , 'body' , 'author']

