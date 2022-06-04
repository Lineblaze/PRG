from django.db import models
from simple_history.models import HistoricalRecords


class Boss(models.Model):
    
    name = models.CharField(verbose_name='Имя' , max_length=40)
    description = models.TextField(verbose_name='Описание')
    healpoints = models.FloatField(verbose_name='Жизни')
    loot = models.CharField(verbose_name='Лут после противника', max_length=40)
    race_b = models.CharField(verbose_name='Раса', max_length=40)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Противник'
        verbose_name_plural = 'Противники'


class Hero(models.Model):
    name_hero = models.CharField(verbose_name='Имя антогониста', max_length=255)
    hp = models.FloatField(verbose_name='Жизни')
    lvl = models.FloatField(verbose_name='Уровень')
    mana = models.FloatField(verbose_name='Мана')
    race = models.CharField(verbose_name='Раса', max_length=40)

    def __str__(self):
        return self.name_hero
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герои'



class Level(models.Model):
    title = models.CharField(verbose_name='Название уровня', max_length=255)
    descr = models.TextField(verbose_name='Описание уровня')
    hero = models.ManyToManyField(Hero, verbose_name='Герой')
    boss = models.ManyToManyField(Boss, verbose_name='Противник')
    experience = models.FloatField(verbose_name='Количесвто опыта')

    history = HistoricalRecords()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровени'
