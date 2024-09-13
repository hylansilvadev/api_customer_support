from rest_framework import serializers

from tiket.models import Tiket

class TiketSerialeizer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tiket
        fields = '__all__'