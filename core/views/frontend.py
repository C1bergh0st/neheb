from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import *
from django.views.generic import TemplateView, DetailView, ListView
import json;
from core.serializers import OrganizationSerializer


#class OrganizationList(APIView):
#    renderer_classes = [TemplateHTMLRenderer]
#    template_name = 'profile_list.html'
#    queryset = Organization.objects.all()
#
#    def get(self, request):
#        queryset = Organization.objects.all()
#        return Response({'profiles': queryset})


class OrganizationView(DetailView):
    model = Organization

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class OrganizationListView(ListView):
    model = Organization
    ordering = ['-name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class ScoreboardView(TemplateView):
    template_name = "core/scoreboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        scoreboard = sorted(Organization.objects.all(), key=lambda t: -t.score)
        context["scoreboard"] = scoreboard
        context["json"] = json.dumps(OrganizationSerializer(scoreboard, many=True).data)
        return context