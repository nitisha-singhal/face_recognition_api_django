from rest_framework import serializers
from .models import PersonMatch


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMatch
        fields = "__all__"
