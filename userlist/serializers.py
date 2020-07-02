from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('user_id', 'user', 'role', 'registration_date')

