from rest_framework import serializers
from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'       
"""
Serializes the Event model for data representation.

Attributes:
    model (Event): The Event model to be serialized.
    fields (list): The fields to be included in the serialized representation.

"""      
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
"""
Serializes the Registration model for data representation.

Attributes:
    model (Registration): The Registration model to be serialized.
    fields (list): The fields to be included in the serialized representation.

"""

