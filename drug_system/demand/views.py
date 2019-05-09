from django.shortcuts import render
from .models import Demander_Demand, Detail, Demand, Demander
from user.models import User


# Create your views here.
def demand(request):
    demands = Demander_Demand.objects.all()
    context = {
        "demand_list": demands,
    }
    # print('context', context)
    return render(request, 'demand/index.html', context)


def submit(request):
    demand_map = request.POST
    lx = User.objects.get(id=1)
    demander = Demander.objects.get(id=1)
    demand_form = Demand(create_user=lx, demander=demander)
    demand_form.save()
    demand_form_list = Demand.objects.all()
    length = demand_form_list.count()  # 获取表数据总长度
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
        length = de_list.count()  # 获取表数据总长度
        detail = de_list[length - 1]
        detail_list.append(detail)
    context = {
        "demand_form": demand_form,
        "detail_list": detail_list,
    }
    return render(request, 'demand/submit.html', context)
