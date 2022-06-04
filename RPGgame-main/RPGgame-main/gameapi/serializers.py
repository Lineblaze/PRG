from rest_framework.serializers import ModelSerializer
from .models import Hero, Boss, Level


class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class BossSerializer(ModelSerializer):
    class Meta:
        model = Boss
        fields = '__all__'

class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
