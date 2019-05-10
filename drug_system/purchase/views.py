from django.shortcuts import render


# Create your views here.
def purchase(request):
    context = {}
    return render(request, 'purchase/index.html', context)


def submit(request):
    pass


def make(request):
    pass


def query(request):
    pass


def query_detail(request, purchase_id):
    pass
