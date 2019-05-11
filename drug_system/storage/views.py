from django.shortcuts import render
from demand.models import Detail, Medicine
from purchase.models import Purchase
from user.models import User
from lack.models import Lack
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Storage


# Create your views here.
def storage(request):
    context = {}
    return render(request, 'storage/index.html', context)


def submit(request):
    demand_map = request.POST
    lx = User.objects.get(id=1)
    storage_form = Storage(create_user=lx)
    storage_form.save()
    storage_form_list = Storage.objects.all()
    length = storage_form_list.count()
    storage_form = storage_form_list[length - 1]
    detail_list = []
    flag = False
    for key in demand_map:
        if not flag:
            flag = True
            continue
        single = Detail.objects.get(id=key)
        single.status = 1
        single.save()
        detail_list.append(single)
    medicines = Medicine.objects.all()
    length = medicines.count()
    medicine = medicines[length - 1]
    medicine_num = medicine.id
    medicine_list = []
    for i in range(medicine_num + 1):
        medicine_list.append(0)
    for detail in detail_list:
        medicine_list[detail.medicine.id] += detail.num
    detail_list2 = []
    for i in range(medicine_num + 1):
        if medicine_list[i] != 0:
            detail = Detail(price=medicine_list[i] * i, num=medicine_list[i], medicine=medicines[i - 1],
                            form_type=5, form_id=storage_form.id)
            detail.save()
            de_list = Detail.objects.all()
            length = de_list.count()
            detail = de_list[length - 1]
            detail_list2.append(detail)
    context = {
        "storage_form": storage_form,
        "detail_list": detail_list2,
    }
    return render(request, 'storage/submit.html', context)


def make(request):
    details = Detail.objects.filter(form_type=4).filter(status=0)
    detail_list = []
    for detail in details:
        purchase = Purchase.objects.get(id=detail.form_id)
        if purchase.status == 1:
            detail_list.append(detail)
    context = {
        "detail_list": detail_list,
    }
    return render(request, 'storage/storage.html', context)


def query(request):
    storage_list = Storage.objects.all()
    status_dict = {
        1: '未入库',
        2: '已入库',
        0: '待审核',
        3: '审核未通过',
    }
    context = {
        'storage_list': storage_list,
        'status_dict': status_dict,
    }
    return render(request, 'storage/query.html', context)


def query(request):
    return HttpResponseRedirect(reverse('storage:query')+'1')


def query_page(request, page_id):
    storage_list = Storage.objects.all().order_by('status', '-id')
    list_length = storage_list.count()
    if page_id*10 >= list_length+10:
        return HttpResponseRedirect(reverse('storage:query') + str((list_length-1) // 10+1))
    storage_list = storage_list[(page_id-1)*10:min(page_id*10, list_length)]
    status_dict = {
        1: '未入库',
        2: '已入库',
        0: '待审核',
        3: '审核未通过',
    }
    context = {
        'storage_list': storage_list,
        'status_dict': status_dict,
        'page_id': page_id,
        'page_id_minus': page_id-1,
        'page_id_plus': page_id+1,
        'page_id_minus2': page_id-2,
        'page_id_minus3': page_id-3,
        'page_id_plus2': page_id+2,
        'page_id_plus3': page_id+3,
    }
    return render(request, 'storage/query.html', context)


def query_detail(request, storage_id):
    detail_list = Detail.objects.filter(form_type=5).filter(form_id=storage_id)
    storage_form = Storage.objects.get(id=storage_id)
    context = {
        'detail_list': detail_list,
        'storage_form': storage_form,
    }
    return render(request, 'storage/submit.html', context)


def accept(request, storage_id):
    storage_form = Storage.objects.get(id=storage_id)
    if storage_form.status != 0:
        return Http404('your operation is not correct!')
    else:
        storage_form.status = 1
        storage_form.save()
        return HttpResponseRedirect(reverse('storage:query'))


def deny(request, storage_id):
    storage_form = Storage.objects.get(id=storage_id)
    if storage_form.status != 0:
        return Http404('your operation is not correct!')
    else:
        detail_list = Detail.objects.filter(form_type=5).filter(form_id=storage_id)
        lx = User.objects.get(id=1)
        lack_form = Lack(create_user=lx)
        lack_form.save()
        lack_form_list = Lack.objects.all()
        length = lack_form_list.count()
        lack_form = lack_form_list[length - 1]
        for detail in detail_list:
            detail_new = Detail(price=detail.price, num=detail.num, medicine=detail.medicine,
                                form_type=3, form_id=lack_form.id)
            detail_new.save()
        storage_form.status = 3
        storage_form.save()
        return HttpResponseRedirect(reverse('storage:query'))


def move(request, storage_id):
    storage_form = Storage.objects.get(id=storage_id)
    if storage_form.status != 1:
        return Http404('your operation is not correct!')
    else:
        detail_list = Detail.objects.filter(form_type=5).filter(form_id=storage_id)
        for detail in detail_list:
            medicine = Medicine.objects.get(id=detail.medicine.id)
            medicine.now_num = medicine.now_num + detail.num
            medicine.save()
        storage_form.status = 2
        storage_form.save()
        return HttpResponseRedirect(reverse('storage:query'))
