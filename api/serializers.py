from rest_framework import serializers
from .models import Voter

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = [
            'ward_no',
            'ac_no',
            'ps_no',
            'sl_no',
            'name',
            'relation_name',
            'relation',
            'age',
            'gender',
            'door_no',
            'epic_no',
        ]
