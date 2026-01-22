import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Voter
from .serializers import VoterSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def search_voter(request):
    q = request.GET.get('q')

    if not q:
        return Response([])

    try:
        voters = Voter.objects.filter(
            Q(epic_no__icontains=q) |
            Q(name__icontains=q) |
            Q(relation_name__icontains=q) |
            Q(door_no__icontains=q)
        )[:50]

        logger.error(f"VOTERS FOUND: {voters.count()}")

        serializer = VoterSerializer(voters, many=True)
        return Response(serializer.data)

    except Exception as e:
        logger.error("SEARCH API FAILED", exc_info=True)
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
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
