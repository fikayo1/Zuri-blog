from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE )
    text = models.TextField()
    created_date = models.DateTimeField()
    publish_date = models.DateTimeField()