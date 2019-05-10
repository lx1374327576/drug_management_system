from django.db import models
from django.utils import timezone
from user.models import User


# Create your models here.
class Storage(models.Model):
    id = models.IntegerField('id', primary_key=True)
    due_time = models.DateTimeField('due_time', default=timezone.now)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField('status', default=0)  # 0 未审核 1 未入库 2 已入库 3 审核未通过
    check_time = models.DateTimeField('check_time', default=timezone.now)
