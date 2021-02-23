from .models import *
from rest_framework import serializers


class RibbonSerializer(serializers.ModelSerializer):
    color = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Ribbon
        fields = ['color', 'weight']

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    score = serializers.ReadOnlyField(read_only=True)
    first_ribbon = RibbonSerializer(read_only=True)
    second_ribbon = RibbonSerializer(read_only=True)
    third_ribbon = RibbonSerializer(read_only=True)
    fourth_ribbon = RibbonSerializer(read_only=True)
    fifth_ribbon = RibbonSerializer(read_only=True)
    # def get_score(self, obj):
    #    return obj.score()

    class Meta:
        model = Organization
        fields = ['name',
                  'pk',
                  'score',
                  'first_ribbon',
                  'second_ribbon',
                  'third_ribbon',
                  'fourth_ribbon',
                  'fifth_ribbon']

