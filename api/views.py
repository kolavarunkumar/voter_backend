from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from django.db.models import Q
from .models import Voter
from .serializers import VoterSerializer

class SearchThrottle(AnonRateThrottle):
    rate = '60/min'

@api_view(['GET'])
@throttle_classes([SearchThrottle])
def search_voter(request):
    q = request.GET.get('q', '').strip()

    if len(q) < 2:
        return Response([])

    voters = Voter.objects.filter(
        Q(epic_no__icontains=q) |
        Q(name__icontains=q) |
        Q(relation_name__icontains=q) |
        Q(door_no__icontains=q)
    )[:50]

    serializer = VoterSerializer(voters, many=True)
    return Response(serializer.data)
