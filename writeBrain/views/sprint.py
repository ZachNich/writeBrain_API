from django.http import HttpResponseServerError
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from writeBrain.models import Sprint
from writeBrain.models import Story
from writeBrain.models import Mood

class SprintSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sprint
        url = serializers.HyperlinkedIdentityField(
            view_name='sprint',
            lookup_field='id'
        )
        fields = ("id", "body", "started_at", "ended_at", "mood_before", "mood_after", "story", "user")
        depth = 1


class Sprints(ViewSet):

    def create(self, request):

        mood_before = Mood.objects.get(pk=request.data['mood_before_id'])
        mood_after = Mood.objects.get(pk=request.data['mood_after_id'])
        story = Story.objects.get(pk=request.data['story_id'])
        user = User.objects.get(pk=request.user.id)

        sprint = Sprint.objects.create(
            body=request.data["body"],
            started_at=request.data["started_at"],
            mood_before=mood_before,
            mood_after=mood_after,
            story=story,
            user=user
        )

        serializer = SprintSerializer(sprint, context={'request': request})

        return Response(serializer.data, content_type='application/json')

    def retrieve(self, request, pk=None):

        try:
            sprint = Sprint.objects.get(pk=pk)
            serializer = SprintSerializer(sprint, many=False, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        sprint = Sprint.objects.get(pk=pk)
        sprint.story = request.data["story"]
        sprint.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            sprint = Sprint.objects.get(pk=pk)
            sprint.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        sprints = Sprint.objects.all()

        serializer = SprintSerializer(sprints, many=True, context={'request': request})

        return Response(serializer.data)