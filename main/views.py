from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView
from . models import Post
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