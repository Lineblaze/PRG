from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from yaml import serialize
from .serializers import HeroSerializer, BossSerializer, LevelSerializer
from .models import Hero, Boss, Level
from rest_framework.generics import ListAPIView, CreateAPIView
import django_filters.rest_framework
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


class HeroViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    @action(methods=['Post'], detail=False, url_path='post') 
    def createGroup(self,request, pk=None):
        hero=self.queryset.create(name_hero=request.data.get('name_hero'))
        hero.save()
        return Response('Succses')


class BossViewSet(ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class GetLevelView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title','boss']


class GetHeroView(ListAPIView):
    queryset = Hero.objects.filter( Q(race='Эльф') | Q(lvl__gt=5) )
    serializer_class = HeroSerializer


class CreateHero(CreateAPIView):
    def post(self, request, format=None):
        serialize = HeroSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return render(serialize.data)

