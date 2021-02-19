from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200 , null= False)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    pub_date = models.TimeField(auto_now=False , auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.pub_date)
