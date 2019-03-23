from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=32)

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/posts/')
    tags = models.ManyToManyField(Tag, blank=True)

