from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserPassword(models.Model):
    website_name = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="passwords")