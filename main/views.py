from django.shortcuts import render
from django.views.generic import ListView , DetailView
from . models import Post
# Create your views here.
#def main(request):
    #return render(request , 'main.html' , {})

class Home(ListView):
    model = Post
    template_name = "main.html"

class Detail(DetailView):
    template_name = "detail.html"