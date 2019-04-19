from django.http import HttpResponse
from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
    except Exception as e:
        return HttpResponse('the user is not available!')
