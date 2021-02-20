from django.urls import path
from . views import Home , Detail , AddPost , UpdatePost

urlpatterns = [
    path('' , Home.as_view() , name='main'),
    path('article/<int:pk>' , Detail.as_view() , name='article'),
    path('create' , AddPost.as_view() , name = "create"),
    path('update/article/<int:pk>' , UpdatePost.as_view() , name="update")
]
