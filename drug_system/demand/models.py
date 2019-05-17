from django.db import models
from django.utils import timezone
from user.models import User


class Medicine_type(models.Model):

    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', blank=False, max_length=100)

    def __str__(self):
        return self.name


class Medicine(models.Model):

    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', blank=False, max_length=100)
    total_num = models.FloatField('total_num', default=0)
    now_num = models.FloatField('now_num', default=0)
    medicine_type = models.ForeignKey(Medicine_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Detail(models.Model):

    id = models.IntegerField('id', primary_key=True)
    father_id = models.IntegerField('father_id', default=0)
    father_detail_id = models.IntegerField('father_detail_id', default=0)
    medicine = models.ForeignKey(Medicine, blank=False, on_delete=models.CASCADE)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    num = models.FloatField('num')
    price = models.FloatField('price')
    status = models.IntegerField('status', default=0)  # 0 未处理 1 处理中 2 已完成
    form_type = models.IntegerField('form_type')  # 1 需求单 2 出库单 3 缺货单 4 采购单 5 入库单
    form_id = models.IntegerField('form_id')


class Demander(models.Model):

    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', blank=False, max_length=100)

    def __str__(self):
        return self.name


class Demand(models.Model):

    id = models.IntegerField('id', primary_key=True)
    due_time = models.DateTimeField('due_time', default=timezone.now)
    demander = models.ForeignKey(Demander, on_delete=models.CASCADE)
    create_time = models.DateTimeField('create_time', default=timezone.now)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField('status', default=0)  # 0 未处理 1 审核通过 2 单子完成 3 审核未通过
    check_time = models.DateTimeField('check_time', default=timezone.now)


class Demander_Demand(models.Model):

    id = models.IntegerField('id', primary_key=True)
    demander = models.ForeignKey(Demander, on_delete=models.CASCADE)
    num = models.FloatField('num')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

