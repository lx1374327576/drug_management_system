from django.shortcuts import render
from .models import Demander_Demand, Detail, Demand, Demander
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
    context = {
        "demand_list": demands,
    }
    # print('context', context)
    return render(request, 'demand/demand.html', context)


def query(request):
    demand_list = Demand.objects.all()
    status_dict = {
        1: '审核通过',
        2: '已完成',
        0: '待审核',
        3: '审核未通过',
    }
    context = {
        'demand_list': demand_list,
        'status_dict': status_dict,
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
