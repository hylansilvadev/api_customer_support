from rest_framework import serializers

from user.models import User

class UserSerialeizer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'