from django.shortcuts import render


# Create your views here.
def checkout(request):
    context = {}
    return render(request, 'checkout/index.html', context)
