from django.http import HttpResponseServerError
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from writeBrain.models import Story

class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        # url = serializers.HyperlinkedIdentityField(
        #     view_name='story',
        #     lookup_field='id'
        # )
        fields = ("id", "title", "description", "user")
        depth = 1


class Stories(ViewSet):

    def create(self, request):

        user = User.objects.get(pk=request.user.id)

        story = Story.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            user=user
        )

        serializer = StorySerializer(story, context={'request': request})
        return Response(serializer.data, content_type='application/json')

    def retrieve(self, request, pk=None):

        try:
            story = Story.objects.get(pk=pk)
            serializer = StorySerializer(story, many=False, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        story = Story.objects.get(pk=pk)
        story.title = request.data["title"]
        story.description = request.data["description"]
        story.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            story = Story.objects.get(pk=pk)
            story.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except story.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        stories = Story.objects.all()

        serializer = StorySerializer(stories, many=True, context={'request': request})

        return Response(serializer.data)