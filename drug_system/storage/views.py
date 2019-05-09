from django.shortcuts import render


# Create your views here.
def storage(request):
    context = {}
    return render(request, 'storage/index.html', context)
