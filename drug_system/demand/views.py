from django.shortcuts import render
from .models import Demander_Demand, Detail, Demand, Demander, Medicine
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from user.models import User


# Create your views here.
def demand(request):
    context = {}
    return render(request, 'demand/index.html', context)


def submit(request):
    demand_map = request.POST
    lx = User.objects.get(id=1)
    demander = Demander.objects.get(id=1)
    demand_form = Demand(create_user=lx, demander=demander)
    demand_form.save()
    demand_form_list = Demand.objects.all()
    length = demand_form_list.count()
    demand_form = demand_form_list[length-1]
    detail_list = []
    flag = False
    for key in demand_map:
        if not flag:
            flag = True
            continue
        single = Demander_Demand.objects.get(id=key)
        detail = Detail(price=single.id*single.num, num=single.num, medicine=single.medicine,
                        form_type=1, form_id=demand_form.id)
        detail.save()
        de_list = Detail.objects.all()
        length = de_list.count()
        detail = de_list[length - 1]
        detail_list.append(detail)
    context = {
        "demand_form": demand_form,
        "detail_list": detail_list,
    }
    return render(request, 'demand/submit.html', context)


def make(request):
    demands = Demander_Demand.objects.all()
    demand_list = Demand.objects.all()
    demand_num = demand_list.count() + 1
    context = {
        "demand_list": demands,
        'demand_num': demand_num,
    }
    # print('context', context)
    return render(request, 'demand/demand.html', context)


def query(request):
    return HttpResponseRedirect(reverse('demand:query')+'1')


def query_page(request, page_id):
    demand_list = Demand.objects.all().order_by('status', '-id')
    list_length = demand_list.count()
    if page_id*10 >= list_length+10:
        return HttpResponseRedirect(reverse('demand:query') + str((list_length-1) // 10+1))
    demand_list = demand_list[(page_id-1)*10:min(page_id*10, list_length)]
    status_dict = {
        1: '审核通过',
        2: '已完成',
        0: '待审核',
        3: '审核未通过',
    }
    context = {
        'demand_list': demand_list,
        'status_dict': status_dict,
        'page_id': page_id,
        'page_id_minus': page_id-1,
        'page_id_plus': page_id+1,
        'page_id_minus2': page_id-2,
        'page_id_minus3': page_id-3,
        'page_id_plus2': page_id+2,
        'page_id_plus3': page_id+3,
    }
    return render(request, 'demand/query.html', context)


def query_detail(request, demand_id):
    detail_list = Detail.objects.filter(form_type=1).filter(form_id=demand_id)
    demand_form = Demand.objects.get(id=demand_id)
    context = {
        'detail_list': detail_list,
        'demand_form': demand_form,
    }
    return render(request, 'demand/submit.html', context)


def deny(request, demand_id):
    demand_form = Demand.objects.get(id=demand_id)
    if demand_form.status != 0:
        return Http404('your operation is not correct!')
    else:
        demand_form.status = 3
        demand_form.save()
        return HttpResponseRedirect(reverse('demand:query'))


def accept(request, demand_id):
    demand_form = Demand.objects.get(id=demand_id)
    if demand_form.status != 0:
        return Http404('your operation is not correct!')
    else:
        demand_form.status = 1
        demand_form.save()
        return HttpResponseRedirect(reverse('demand:query'))


def make_input(request):
    medicine_list = Medicine.objects.all()
    demander_list = Demander.objects.all()
    demand_list = Demand.objects.all()
    demand_num = demand_list.count() + 1
    context = {
        'medicine_list': medicine_list,
        'demander_list': demander_list,
        'demand_num': demand_num,
    }
    return render(request, 'demand/make_input.html', context)


def submit_input(request):
    medicine_map = request.POST
    lx = User.objects.get(id=1)
    demander_id = medicine_map['demander_id']
    demander = Demander.objects.get(id=demander_id)
    demand_form = Demand(create_user=lx, demander=demander)
    demand_form.save()
    demand_form_list = Demand.objects.all()
    length = demand_form_list.count()
    demand_form = demand_form_list[length - 1]
    for key in medicine_map:
        test = -1
        if key == 'demander_id':
            continue
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
            detail = Detail(price=medicine_id * medicine_num, num=medicine_num, medicine=medicine,
                            form_type=1, form_id=demand_form.id)
            detail.save()
    detail_list = Detail.objects.filter(form_type=1).filter(form_id=demand_form.id)
    context = {
        "demand_form": demand_form,
        "detail_list": detail_list,
    }
    return render(request, 'demand/submit.html', context)
