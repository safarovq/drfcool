from rest_framework import serializers
from .models import Boys


class BoysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boys
        fields = ('name', 'descriptions',)
