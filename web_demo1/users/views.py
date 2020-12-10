from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import web_db

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # users = web_db.objects.create(username=username, password=password)
        import json
        req_dict = json.loads(request.body)

        username = req_dict.get('username')
        password = req_dict.get('password')
        user = web_db.objects.create(username=username, password=password)
        return redirect('/login/')

def login(request):
    username = request.POST.get('username')
    if username:
        return HttpResponse(f'{username}已经登录过了')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            users = web_db.objects.get(username=username, password=password)
        except web_db.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            if remember != 'true':
                request.session.set_expiry(0)
            return JsonResponse({'meassage': 'login sucess'})

def user_info(request, id):
    try:
        user =web_db.objects.get(id=id)
    except web_db.DoesNotExist:
        return JsonResponse({'message': '用户不存在'})
    else:
        res_data = {
            'id': user.id,
            'name': user.username,
            'age': user.age
        }
        return JsonResponse(res_data)