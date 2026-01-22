import logging
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from django.db.models import Q
from .models import Voter
from .serializers import VoterSerializer

logger = logging.getLogger(__name__)

class SearchThrottle(AnonRateThrottle):
    rate = '60/min'

@api_view(['GET'])
@throttle_classes([SearchThrottle])
def search_voter(request):
    q = request.GET.get('q', '').strip()
    logger.info(f"Search called with query: '{q}'")

    if len(q) < 2:
        return Response([])

    try:
        voters = Voter.objects.filter(
            Q(epic_no__icontains=q) |
            Q(name__icontains=q) |
            Q(relation_name__icontains=q) |
            Q(door_no__icontains=q)
        )[:50]
        logger.info(f"Found {voters.count()} voters matching '{q}'")
        serializer = VoterSerializer(voters, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.exception(f"Search failed for query '{q}'")
        return Response({'error': 'Internal Server Error'}, status=500)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Voter

@api_view(['GET'])
def test_db(request):
    try:
        total = Voter.objects.count()
        sample = Voter.objects.first()
        return Response({
            'total_voters': total,
            'sample_voter': {
                'epic_no': sample.epic_no,
                'name': sample.name
            } if sample else None
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)
