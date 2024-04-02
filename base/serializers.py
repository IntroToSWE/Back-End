from rest_framework import serializers
from . models import *

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["first_name", "last_name", "email", "password"]