import datetime
import random
import string

from django.db import models
from django.utils import timezone


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class User(models.Model):
    email = models.EmailField('электронная почта',
                              unique=True)
    user_id = models.CharField('ID',
                               default=id_generator(50, string.ascii_lowercase + string.digits),
                               max_length=50)
    username = models.CharField('никнейм',
                                max_length=40)
    password = models.CharField('пароль',
                                max_length=40)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.username


class Game(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              default='1')
    game_id = models.CharField('ID',
                               default=id_generator(50, string.ascii_lowercase + string.digits),
                               max_length=50,
                               primary_key=True,
                               unique=True)
    game_tag = models.CharField('тэг',
                                max_length=5,
                                default=id_generator(5, string.ascii_uppercase + string.digits))
    game_name = models.CharField('название',
                                 max_length=50,
                                 default='Игра',
                                 unique=True)
    game_present_cost_min = models.IntegerField('минимальная стоимость подарка',
                                                default=200)
    game_present_cost_max = models.IntegerField('максимальная стоимость подарка',
                                                default=1000)
    pub_date = models.DateField('дата начала игры',
                                auto_now_add=True)
    game_timer = models.IntegerField('длительность игры',
                                     default=5)
    # gamers_number =

    def __str__(self):
        return self.game_name

    def hasended(self):
        return self.pub_date < timezone.now() - datetime.timedelta(days=self.game_timer)

    class Meta:
        ordering = ["pub_date", "game_name"]
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Gamer(models.Model):
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,
                             default='1')
    gamer_id = models.CharField('ID',
                                default=id_generator(50, string.ascii_lowercase + string.digits),
                                primary_key=True,
                                max_length=50,
                                unique=True)
    gamer_name = models.CharField('имя игрока',
                                  max_length=20)

    def __str__(self):
        return self.gamer_name

    class Meta:
        verbose_name = 'Игроки'
        verbose_name_plural = 'Игрок'
