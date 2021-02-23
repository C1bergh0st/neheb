from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import *
from .serializers import OrganizationSerializer, RibbonSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organization.objects.all().order_by('-name')
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class RibbonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ribbon.objects.all()
    serializer_class = RibbonSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def organization_scoreboard(request):
    scoreboard = sorted(Organization.objects.all(), key=lambda t: -t.score)
    return Response(OrganizationSerializer(scoreboard, many=True).data)