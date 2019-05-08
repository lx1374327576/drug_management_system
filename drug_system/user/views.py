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
    return render(request, 'user/index.html', context)


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
