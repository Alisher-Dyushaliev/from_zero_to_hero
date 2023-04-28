from rest_framework import serializers
from .models import Newskg

class LangsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Newskg
        fields = '__all__'