from django.shortcuts import render


# Create your views here.
def lack(request):
    context = {}
    return render(request, 'lack/index.html', context)
