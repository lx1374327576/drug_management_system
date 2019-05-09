from django.db import models
from user.models import User
from django.utils import timezone


# Create your models here.
class Checkout(models.Model):
    id = models.IntegerField('id', primary_key=True)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField('status', default=0)  # 0 待出库 1 已出库
