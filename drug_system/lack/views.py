from django.shortcuts import render
from checkout.models import Checkout
from demand.models import Detail, Medicine
from user.models import User
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Lack


# Create your views here.
def lack(request):
    context = {}
    return render(request, 'lack/index.html', context)


def make(request):
    details = Detail.objects.filter(form_type=2).filter(status=0)
    detail_list = []
    for detail in details:
        checkout = Checkout.objects.get(id=detail.form_id)
        if checkout.status == 1:
            detail_list.append(detail)
    context = {
        "detail_list": detail_list,
    }
    return render(request, 'lack/lack.html', context)


def submit(request):
    demand_map = request.POST
    lx = User.objects.get(id=1)
    lack_form = Lack(create_user=lx)
    lack_form.save()
    lack_form_list = Lack.objects.all()
    length = lack_form_list.count()
    lack_form = lack_form_list[length - 1]
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
    medicine = medicines[length-1]
    medicine_num = medicine.id
    medicine_list = []
    for i in range(medicine_num+1):
        medicine_list.append(0)
    for detail in detail_list:
        medicine_list[detail.medicine.id] += detail.num
    detail_list2 = []
    for i in range(medicine_num+1):
        if medicine_list[i] != 0:
            detail = Detail(price=medicine_list[i]*i, num=medicine_list[i], medicine=medicines[i-1],
                            form_type=3, form_id=lack_form.id)
            medicine = Medicine.objects.get(id=medicines[i-1].id)
            medicine.total_num = medicine.total_num + medicine_list[i]
            medicine.save()
            detail.save()
            de_list = Detail.objects.all()
            length = de_list.count()
            detail = de_list[length - 1]
            detail_list2.append(detail)
    context = {
        "lack_form": lack_form,
        "detail_list": detail_list2,
    }
    return render(request, 'lack/submit.html', context)


def query(request):
    return HttpResponseRedirect(reverse('lack:query') + '1')


def query_page(request, page_id):
    lack_list = Lack.objects.all().order_by('-id')
    list_length = lack_list.count()
    if page_id * 10 >= list_length + 10:
        return HttpResponseRedirect(reverse('lack:query') + str((list_length - 1) // 10 + 1))
    lack_list = lack_list[(page_id - 1) * 10:min(page_id * 10, list_length)]
    context = {
        'lack_list': lack_list,
        'page_id': page_id,
        'page_id_minus': page_id - 1,
        'page_id_plus': page_id + 1,
        'page_id_minus2': page_id - 2,
        'page_id_minus3': page_id - 3,
        'page_id_plus2': page_id + 2,
        'page_id_plus3': page_id + 3,
    }
    return render(request, 'lack/query.html', context)


def query_detail(request, lack_id):
    detail_list = Detail.objects.filter(form_type=3).filter(form_id=lack_id)
    lack_form = Lack.objects.get(id=lack_id)
    context = {
        'detail_list': detail_list,
        'lack_form': lack_form,
    }
    return render(request, 'lack/submit.html', context)


def stack(request):
    medicine_list = Medicine.objects.all()
    context = {
        'medicine_list': medicine_list,
    }
    return render(request, 'lack/stack.html', context)


def stack_submit(request):
    medicine_map = request.POST
    lx = User.objects.get(id=1)
    lack_form = Lack(create_user=lx)
    lack_form.save()
    lack_form_list = Lack.objects.all()
    length = lack_form_list.count()
    lack_form = lack_form_list[length - 1]
    for key in medicine_map:
        test = -1
        try:
            test = int(medicine_map[key])
        except Exception:
            print('key:', key, 'map[key]:', medicine_map[key])
        if test <= 0:
            continue
        else:
            medicine_id = int(key)
            medicine_num = test
            medicine = Medicine.objects.get(id=medicine_id)
            medicine.total_num = medicine.total_num + medicine_num
            medicine.save()
            detail = Detail(price=medicine_num*medicine_id, num=medicine_num, medicine=medicine,
                            form_type=3, form_id=lack_form.id)
            detail.save()
    return HttpResponseRedirect(reverse('lack:query'))
