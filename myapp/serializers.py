from rest_framework import serializers
from .models import PersonModel

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'