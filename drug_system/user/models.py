from django.db import models
from django.utils import timezone


class User(models.Model):

    id = models.IntegerField('id', primary_key=True)
    user_name = models.CharField('user_name', unique=True, blank=False, max_length=20)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    is_admin = models.BooleanField('is_admin', default=False)
    password = models.CharField('password', blank=False, max_length=20)
    worker_type = models.IntegerField('worker_type', default=0)

    def __str__(self):
        return self.user_name
