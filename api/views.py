# api/views.py

from rest_framework.decorators import api_view, throttle_classes 
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from django.db.models import Q
from .models import Voter
from .serializers import VoterSerializer

import logging

# Set up logger
logger = logging.getLogger(__name__)

# Throttle class
class SearchThrottle(AnonRateThrottle):
    rate = '60/min'

@api_view(['GET'])
@throttle_classes([SearchThrottle])
def search_voter(request):
    try:
        # Log incoming request
        logger.info(f"Incoming search request from {request.META.get('REMOTE_ADDR')} with params: {request.GET}")

        # Get query parameter
        q = request.GET.get('q', '').strip()

        if len(q) < 2:
            logger.warning(f"Query too short: '{q}'")
            return Response([])

        # Perform search
        voters = Voter.objects.filter(
            Q(epic_no__icontains=q) |
            Q(name__icontains=q) |
            Q(relation_name__icontains=q) |
            Q(door_no__icontains=q)
        )[:50]

        logger.info(f"Found {voters.count()} voters for query '{q}'")

        # Serialize results
        serializer = VoterSerializer(voters, many=True)
        return Response(serializer.data)

    except Exception as e:
        # Log full exception
        logger.error(f"Search query error for '{q}': {e}", exc_info=True)
        return Response({'error': 'Internal Server Error'}, status=500)
