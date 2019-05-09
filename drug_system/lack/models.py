from django.db import models
from django.utils import timezone
from user.models import User


# Create your models here.
class Lack(models.Model):
    id = models.IntegerField('id', primary_key=True)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
