from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserPassword(models.Model):
    website_name = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="passwords")

    def __str__(self):
        return "{ Website Name: " + self.website_name + ", Password: " + self.password + " }"