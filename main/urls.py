from django.urls import path
from . views import Home , Detail

urlpatterns = [
    path('' , Home.as_view() , name='main'),
    path('/detail' , Detail.as_view() , name='detail'),
]
