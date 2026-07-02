from rest_framework import serializers
from . import models

class AdSerializer(serializers.ModelSerializer):
    publisher=serializers.ReadOnlyField(source='publisher.username')
    class Meta:
        model=models.Ad
        fields='__all__'
        read_only_fields=('id','date_added','is_public','publisher')
        extra_kwargs={'image': {'required':False}}
    