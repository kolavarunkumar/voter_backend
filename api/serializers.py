from rest_framework import serializers
from .models import Voter

class VoterSerializer(serializers.ModelSerializer):
    ward_no = serializers.IntegerField(required=False, allow_null=True)
    ac_no = serializers.IntegerField(required=False, allow_null=True)
    ps_no = serializers.IntegerField(required=False, allow_null=True)
    sl_no = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    relation_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    relation = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    age = serializers.IntegerField(required=False, allow_null=True)
    gender = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    door_no = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    epic_no = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Voter
        fields = '__all__'
