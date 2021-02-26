from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import *

class OrganizationList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'
    queryset = Organization.objects.all()

    def get(self, request):
        queryset = Organization.objects.all()
        return Response({'profiles': queryset})