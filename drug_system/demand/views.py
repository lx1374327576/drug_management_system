from django.shortcuts import render


# Create your views here.
def demand(request):
    context = {}
    return render(request, 'demand/index.html', context)
