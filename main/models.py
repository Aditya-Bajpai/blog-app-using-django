from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import date  , datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200 , null= False)
    author = models.ForeignKey(User , on_delete=models.CASCADE , default="Author Unkown")
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article' , args = (str(self.id)))
        return reverse('main')
