from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Actor
from rest_framework import filters
from django_filters import rest_framework as filters1
from .serializers import *


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters1.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['genre']
    ordering_fields = ['imdb']

    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs):
        movies = self.get_object()
        actors_id = self.request.data['pk']
        actor = Actor.objects.get(pk=actors_id)
        movies.actor.add(actor)
        movies.save()
        return Response({'status': 'Muvafaqqiyatli qoshildi'})

    @action(detail=True, methods=["POST"])
    def remove_actor(self, request, *args, **kwargs):
        movies = self.get_object()
        actors_id = request.data['pk']
        actor = Actor.objects.get(pk=actors_id)
        movies.actor.remove(actor)
        movies.save()
        return Response({'status': 'Muvafaqqiyatli ochirildi'})

    @action(detail=True, methods=['GET'])
    def actor_list(self, request, *args, **kwargs):
        movies = self.get_object()
        serializer = ActorSerializer(movies.actor.all(), many=True)
        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        comment = Comment.objects.filter(user_id=self.request.user)
        serializer = CommentSerializer(comment, many=True)
        return Response(data=serializer.data)
