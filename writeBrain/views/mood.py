from django.http import HttpResponseServerError
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from writeBrain.models import Mood

class MoodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mood
        url = serializers.HyperlinkedRelatedField(
            view_name='mood',
            lookup_field='id',
            read_only='True'
        )
        fields = ("id", "name")


class Moods(ViewSet):
    def retrieve(self, request, pk=None):

        try:
            mood = Mood.objects.get(pk=pk)
            serializer = MoodSerializer(mood, many=False, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        moods = Mood.objects.all()

        serializer = MoodSerializer(moods, many=True, context={'request': request})

        return Response(serializer.data)
