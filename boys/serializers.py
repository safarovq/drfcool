import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Boys


class BoysModel:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class BoysSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


def encode():
    model = BoysModel(name='Khabib', description='Khabib description')
    serializer = BoysSerializer(data=model.__dict__)  # Pass the model instance as data
    serializer.is_valid()  # Validate the serializer
    serialized_data = serializer.data
    print(serialized_data, type(serialized_data), sep="\n")
    json = JSONRenderer().render(serialized_data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"name":"Khabib","description":"Khabib description"}')
    data = JSONParser().parse(stream)
    serializer = BoysSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)

# class BoysSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Boys
#         fields = ('name', 'descriptions',)
