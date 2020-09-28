from django.http import HttpResponseServerError
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from writeBrain.models import Sprint
from writeBrain.models import Story
from writeBrain.models import Mood
from writeBrain.helpers import analyze

class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
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
            ended_at=request.data["ended_at"],
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
            analysis = analyze(sprint.body)
            serializer = SprintSerializer(sprint, many=False, context={'request': request})
            return JsonResponse({"data": serializer.data, "analysis": analysis})

        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        sprint = Sprint.objects.get(pk=pk)
        sprint.story = Story.objects.get(pk=request.data["story_id"])
        sprint.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            sprint = Sprint.objects.get(pk=pk)
            sprint.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except sprint.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        sprints = Sprint.objects.all()
        story = self.request.query_params.get('story', None)

        if request.user.id:
            sprints = sprints.filter(user__id=request.user.id)
        if story is not None:
            sprints = sprints.filter(story__id=story)
            
        serializer = SprintSerializer(sprints, many=True, context={'request': request})

        return Response(serializer.data)