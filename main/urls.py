from django.urls import path
from . views import Home , Detail , AddPost

urlpatterns = [
    path('' , Home.as_view() , name='main'),
    path('article/<int:pk>' , Detail.as_view() , name='article'),
    path('create' , AddPost.as_view() , name = "create"),
]
