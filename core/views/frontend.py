from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from core.models import *
from django.views.generic import TemplateView, DetailView, ListView, View
import json;
from core.serializers import OrganizationSerializer
from core.forms import UserForm
from django.core.exceptions import ObjectDoesNotExist

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

class UserView(View):
    def post(self, request,  **kwargs):
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            attendee = None
            message = None
            try:
                possible_match = Attendee.objects.get(name=form.cleaned_data['name'])
            except ObjectDoesNotExist:
                return render(request, 'core/history.html', {'form': form, 'msg': "No user with this name"})

            if possible_match.token == form.cleaned_data['token']:
                attendee = possible_match
            else:
                return render(request, 'core/history.html', {'form': form, 'msg': "Wrong token"})

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'core/history.html', {'form': form, 'attendee': attendee})

    def get(self, request, **kwargs):
        form = UserForm()
        return render(request, 'core/history.html', {'form': form})