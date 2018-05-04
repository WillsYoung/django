import random, time

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
# 导入自己写的users模块
from uauth.models import Users
# 导入系统自带的users
from django.contrib.auth.models import User


def regiter(request):

    if request.method == 'GET':
        return render(request, 'day6_regist.html')

    if request.method == 'POST':
        # 注册
        name = request.POST.get('name')
        password = request.POST.get('password')

        # 对密码进行加密
        password = make_password(password)

        Users.objects.create(u_name=name, u_password=password)

        return HttpResponseRedirect('/u/login/')


def my_login(request):
    if request.method == 'GET':
        return render(request, 'day6_login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到Cookie， set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Users.objects.filter(u_name=name).exists():
            user = Users.objects.get(u_name=name)
            if check_password(password, user.u_password):
                ticket = ''
                for i in range(15):
                    ticket += random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
                now_time = int(time.time())
                ticket = 'TK_' + ticket + str(now_time)
                # 绑定令牌到本地浏览器Cookie里面
                response = HttpResponseRedirect('/s/index/')
                # max_age表示这个Cookie的存在时间为50s，超过时间则需要重新登录
                response.set_cookie('ticket', ticket, max_age=5000)
                # 存令牌到服务端
                user.u_ticket = ticket
                user.save()
                return response
            else:
                return HttpResponse('用户密码错误')
        else:
            return HttpResponse('用户不存在')


# 使用django自带的
def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        r = request.POST
        name = r['name']
        password = r['password']

        user = auth.authenticate(username=name, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/s/index/')
        else:
            return HttpResponse('用户名或密码错误。')


def logout(request):

    if request.method == 'GET':
        response = HttpResponseRedirect('/u/login/')
        response.delete_cookie('ticket')
        return response


def djlogin(request):
    if request.method == 'GET':
        return render(request, "login.html")
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # 验证用户名和密码，验证通过返回user对象
        user = auth.authenticate(username=name, password=password)
        if user:
            # 验证成功
            auth.login(request, user)
            return HttpResponseRedirect('/s/index/')
        else:
            return HttpResponse('用户名或者密码错误')


def djregist(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')

        User.objects.create_user(username=name, password=password)
        return HttpResponseRedirect('/u/dj_login/')


def djlogout(request):

    if request.method == 'GET':
        auth.logout(request)

        return HttpResponseRedirect('/u/dj_login/')