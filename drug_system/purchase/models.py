from django.db import models
from django.utils import timezone
from user.models import User


# Create your models here.
class Provider(models.Model):

    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', blank=False, max_length=100)
    address = models.CharField('address', blank=False, max_length=100)

    def __str__(self):
        return self.name


class Purchase(models.Model):

    id = models.IntegerField('id', primary_key=True)
    due_time = models.DateTimeField('due_time', default=timezone.now)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField('status', default=0)  # 0 未处理 1 审核通过 2 单子完成 3 审核未通过
    check_time = models.DateTimeField('check_time', default=timezone.now)
