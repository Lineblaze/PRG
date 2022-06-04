from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BossViewSet, CreateHero, HeroViewSet, LevelViewSet, GetHeroView, GetLevelView

router = DefaultRouter()
router.register('boss', BossViewSet, )
router.register('hero', HeroViewSet, )
router.register('level', LevelViewSet, )




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/hero/filtering', GetHeroView.as_view()),
    path('api/hero/create', CreateHero.as_view()),
    path('api/level/filtering', GetLevelView.as_view()),
]
