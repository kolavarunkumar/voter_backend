from rest_framework import serializers
from .models import Voter


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        exclude = ['id']
