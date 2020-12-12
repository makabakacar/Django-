from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import WebDb
from django.utils.decorators import method_decorator
from django.views import View
from django.utils.decorators import method_decorator


def is_login(view_func):
    def wrapper(request):
        username = request.session.get('username')
        if username:
            return JsonResponse({f'{username}已经登录'})
        return view_func(request)
    return wrapper


class IsLoginMiXin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view_func = super().as_view(**initkwargs)
        return is_login(view_func)


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = WebDb.objects.create(username=username, password=password)
        return redirect('/login/')


class LoginView(IsLoginMiXin, View):

    # @method_decorator(is_login)
    def get(self, request):
        return render(request, 'login.html')

    # @method_decorator(is_login)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            users = WebDb.objects.get(username=username, password=password)
        except WebDb.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            # response = JsonResponse({'message': 'login success'})
            # if remember == 'true':
            #     response.set_cookie('username', username, 60*60*24)
            # return response
            request.session['user_id'] = users.id
            request.session['username'] = users.username
            if remember != 'true':
                request.session.set_expiry(0)
            return JsonResponse({'message': 'login success'})

