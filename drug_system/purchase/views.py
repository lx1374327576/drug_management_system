from django.shortcuts import render


# Create your views here.
def purchase(request):
    context = {}
    return render(request, 'purchase/index.html', context)
