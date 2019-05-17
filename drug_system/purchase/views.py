from django.shortcuts import render
from demand.models import Detail, Medicine
from user.models import User
from .models import Purchase, Provider
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def purchase(request):
    context = {}
    return render(request, 'purchase/index.html', context)


def submit(request):
    demand_map = request.POST
    detail_list = []
    provider_id = 0
    flag = 0
    for key in demand_map:
        if flag == 0:
            flag += 1
            continue
        elif flag == 1:
            flag += 1
            provider_id = demand_map[key]
            continue
        single = Detail.objects.get(id=key)
        single.status = 1
        single.save()
        detail_list.append(single)
    lx = User.objects.get(id=1)
    provider = Provider.objects.get(id=provider_id)
    purchase_form = Purchase(create_user=lx, provider=provider)
    purchase_form.save()
    purchase_form_list = Purchase.objects.all()
    length = purchase_form_list.count()
    purchase_form = purchase_form_list[length-1]
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
                            form_type=4, form_id=purchase_form.id)
            detail.save()
            de_list = Detail.objects.all()
            length = de_list.count()
            detail = de_list[length - 1]
            detail_list2.append(detail)
    context = {
        "purchase_form": purchase_form,
        "detail_list": detail_list2,
    }
    return render(request, 'purchase/submit.html', context)


def make(request):
    details = Detail.objects.filter(form_type=3).filter(status=0)
    provider_list = Provider.objects.all()
    detail_list = []
    for detail in details:
        detail_list.append(detail)
    purchase_list = Purchase.objects.all()
    purchase_num = purchase_list.count() + 1
    context = {
        "detail_list": detail_list,
        "provider_list": provider_list,
        "purchase_num": purchase_num,
    }
    return render(request, 'purchase/purchase.html', context)


def query(request):
    return HttpResponseRedirect(reverse('purchase:query')+'1')


def query_page(request, page_id):
    purchase_list = Purchase.objects.all().order_by('status', '-id')
    list_length = purchase_list.count()
    if page_id*10 >= list_length+10:
        return HttpResponseRedirect(reverse('purchase:query') + str((list_length-1) // 10+1))
    purchase_list = purchase_list[(page_id-1)*10:min(page_id*10, list_length)]
    status_dict = {
        1: '审核通过',
        2: '已完成',
        0: '待审核',
        3: '审核未通过',
    }
    context = {
        'purchase_list': purchase_list,
        'status_dict': status_dict,
        'page_id': page_id,
        'page_id_minus': page_id-1,
        'page_id_plus': page_id+1,
        'page_id_minus2': page_id-2,
        'page_id_minus3': page_id-3,
        'page_id_plus2': page_id+2,
        'page_id_plus3': page_id+3,
    }
    return render(request, 'purchase/query.html', context)


def query_detail(request, purchase_id):
    detail_list = Detail.objects.filter(form_type=4).filter(form_id=purchase_id)
    purchase_form = Purchase.objects.get(id=purchase_id)
    context = {
        'detail_list': detail_list,
        'purchase_form': purchase_form,
    }
    return render(request, 'purchase/submit.html', context)


def accept(request, purchase_id):
    purchase_form = Purchase.objects.get(id=purchase_id)
    if purchase_form.status != 0:
        return Http404('your operation is not correct!')
    else:
        purchase_form.status = 1
        purchase_form.save()
        return HttpResponseRedirect(reverse('purchase:query'))


def deny(request, purchase_id):
    purchase_form = Purchase.objects.get(id=purchase_id)
    if purchase_form.status != 0:
        return Http404('your operation is not correct!')
    else:
        purchase_form.status = 3
        purchase_form.save()
        return HttpResponseRedirect(reverse('purchase:query'))
