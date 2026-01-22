# api/views.py

from rest_framework.decorators import api_view, throttle_classes 
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from django.db.models import Q
from .models import Voter
from .serializers import VoterSerializer

import logging  # logging import at top
logger = logging.getLogger(__name__)  # define logger after imports

# Define your throttle class BEFORE using it
class SearchThrottle(AnonRateThrottle):
    rate = '60/min'

@api_view(['GET'])
@throttle_classes([SearchThrottle])  # <-- use throttle AFTER it is defined
def search_voter(request):
    try:
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

    except Exception as e:
        logger.error(f"Search query error for '{q}': {e}", exc_info=True)
        return Response({'error': 'Internal Server Error'}, status=500)
