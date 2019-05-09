from django.shortcuts import render
from demand.models import Detail, Demand
from user.models import User
from .models import Checkout
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def checkout(request):
    context = {}
    return render(request, 'checkout/index.html', context)


def make(request):
    details = Detail.objects.filter(form_type=1).filter(status=0)
    detail_list = []
    for detail in details:
        demand = Demand.objects.get(id=detail.form_id)
        if demand.status == 1:
            detail_list.append(detail)
    context = {
        "detail_list": detail_list,
    }
    return render(request, 'checkout/checkout.html', context)


def submit(request):
    demand_map = request.POST
    lx = User.objects.get(id=1)
    checkout_form = Checkout(create_user=lx)
    checkout_form.save()
    checkout_form_list = Checkout.objects.all()
    length = checkout_form_list.count()
    checkout_form = checkout_form_list[length - 1]
    detail_list = []
    flag = False
    for key in demand_map:
        if not flag:
            flag = True
            continue
        single = Detail.objects.get(id=key)
        single.status = 1
        single.save()
        detail = Detail(price=single.price, num=single.num, medicine=single.medicine,
                        form_type=2, form_id=checkout_form.id, father_id=single.form_id, father_detail_id=single.id)
        detail.save()
        de_list = Detail.objects.all()
        length = de_list.count()
        detail = de_list[length - 1]
        detail_list.append(detail)
    context = {
        "checkout_form": checkout_form,
        "detail_list": detail_list,
    }
    return render(request, 'Checkout/submit.html', context)


def query(request):
    checkout_list = Checkout.objects.all()
    status_dict = {
        1: '已出库',
        0: '未出库',
    }
    context = {
        'checkout_list': checkout_list,
        'status_dict': status_dict,
    }
    return render(request, 'checkout/query.html', context)


def query_detail(request, checkout_id):
    detail_list = Detail.objects.filter(form_type=2).filter(form_id=checkout_id)
    checkout_form = Demand.objects.get(id=checkout_id)
    context = {
        'detail_list': detail_list,
        'checkout_form': checkout_form,
    }
    return render(request, 'checkout/submit.html', context)


def move(request, checkout_id):
    checkout = Checkout.objects.get(id=checkout_id)
    if checkout.status != 0:
        return Http404('your operation is not correct!')
    else:
        checkout.status = 1
        checkout.save()
        return HttpResponseRedirect(reverse('checkout:query'))
