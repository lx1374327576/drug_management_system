from django.shortcuts import render
from .models import Demander_Demand


# Create your views here.
def demand(request):
    demands = Demander_Demand.objects.all()
    context = {
        "demand_list": demands,
    }
    print('context', context)
    return render(request, 'demand/index.html', context)


def submit(request):
    pass
