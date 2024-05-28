from rest_framework import serializers
from .models import UserPassword

class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPassword
        fields = ["id","website_name","website_url","username","password","last_modified","user"]
        extra_kwargs = {"user": {"read_only":True}}
