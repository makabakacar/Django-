from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import web_db
from django.views import View
# import  hashlib
# a = hashlib.md5()

# Create your views here.
# def register(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     else:
#         # name = request.POST.get('username')
#         # pwd = request.POST.get('password')
#         # web_db.objects.create(username=name, password=pwd)
#         # return redirect('/login/')
#         import json
#         req_dict = json.loads(request.body)
#         username = req_dict.get('username')
#         password = req_dict.get('password')
#         web_db.objects.create(username=username, password=password)
#         return redirect('/login/')


class RegisterView(View):

    def get(self, request):
        if request.method == 'GET':
            return render(request, 'register.html')
        else:
            # name = request.POST.get('username')
            # pwd = request.POST.get('password')
            # web_db.objects.create(username=name, password=pwd)
            # return redirect('/login/')
            import json
            req_dict = json.loads(request.body)
            username = req_dict.get('username')
            password = req_dict.get('password')
            web_db.objects.create(username=username, password=password)
            return redirect('/login/')


class LoginView(View):

    def get(self, request):
        username = request.session.get('username')

        if username:
            return HttpResponse(f'{username}已经登录')

        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = web_db.objects.get(username=username, password=password)
        except web_db.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            if remember != 'true':
                request.session.set_expiry(0)
            return JsonResponse({'message': 'login success'})
# def login(request):
#
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         name = request.POST.get('username')
#         pwd = request.POST.get('password')
#         remember = request.POST.get('remember')
#         try:
#             user = web_db.objects.get(username=name, password=pwd)
#
#         except web_db.DoesNotExist:
#             return JsonResponse({'message': 'login failed'})
#         else:
#             # return JsonResponse({'message': 'login success'})
#             """cookies创建"""
#             # response = HttpResponse({'message': 'login success'})
#             # if remember == 'true':
#             #     response.set_cookie('username', name, max_age= 60*60)
#             #
#             # """ session 中保存当前登录用户的信息 """
#             request.session['user_id'] = user.id
#             request.session['username'] = user.username
#             if remember != 'true':
#                 request.session.set_expiry(0)
#             return JsonResponse({'message': 'login success'})
#             # return response

""" 当服务器返回的是url地址时, 可以获取指定用户的信息 """
def user_info(request, id):
    try:
        user = web_db.objects.get(id=id)
    except web_db.DoesNotExist:
        return JsonResponse({'message': '用户不存在'})
    else:
        # 通过 json 返回用户的信息数据
        res_data = {
            'id': user.id,
            'username': user.username,
            'age': user.age
        }
        return JsonResponse(res_data)

# def user_info(request, id):
#     try:
#         user = web_db.objects.get(id=id)
#     except web_db.DoesNotExist:
#         return JsonResponse({'message': '用户不存在'})
#     else:
#         res_data = {
#             'id': user.id,
#             'name': user.username,
#             'gender': user.gender,
#             'age': user.age
#         }
#         return JsonResponse(res_data)
