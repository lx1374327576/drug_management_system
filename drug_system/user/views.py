from django.http import HttpResponse
from django.http import Http404
from .models import User
from django.template import loader
from django.shortcuts import render


def index(request):
    user_list = list(User.objects.all())
    context = {
        'user_list': user_list,
    }
    return render(request, 'user/test.html', context)


def query(request, id, query_name):
    try:
        q = User.objects.get(id=id)
        if query_name == 'is_admin':
            if q.is_admin:
                return HttpResponse('%s is admin!' % q.user_name)
            else:
                return HttpResponse('%s isn\'t admin!' % q.user_name)
        elif query_name == 'find_username':
            return HttpResponse('id %d is %s' % (q.id, q.user_name))
        else:
            return HttpResponse('query_name is incorrect!')
    except User.DoesNotExist:
        raise Http404('user is not exist!')
    except Exception as e:
        return HttpResponse('the user is not available!')


def login(request):
    try:
        user_name = request.POST['user_name']
        password = request.POST['password']
        q = User.objects.get(user_name=user_name)
        if q.password != password:
            return HttpResponse('Password is Wrong!')
        else:
            context = {
                'user': q,
            }
            return render(request, 'user/index.html', context)
    except Exception as e:
        print(e)
        return HttpResponse('Something went wrong')


def demand(request):
    context = {}
    return render(request, 'demand/index.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout/index.html', context)


def lack(request):
    context = {}
    return render(request, 'lack/index.html', context)


def purchase(request):
    context = {}
    return render(request, 'purchase/index.html', context)


def storage(request):
    context = {}
    return render(request, 'storage/index.html', context)
