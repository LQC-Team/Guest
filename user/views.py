from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


from .models import User

from utils.mixin import LoginRequiredMixin

import re


# /user/register
class RegisterView(View):
    '''注册'''

    def get(self, request):
        '''显示注册页面'''
        return render(request, 'register.html')

    def post(self, request):
        '''进行注册处理'''
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 进行业务处理: 进行用户注册
        user = User.objects.create_user(username, email, password)
        user.save()

        # 返回应答, 跳转到首页
        return redirect('user:login')


# /user/login
class LoginView(View):
    '''登录'''

    def get(self, request):
        '''显示登录页面'''
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        # 使用模板
        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        '''登录校验'''
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理:登录校验
        user = authenticate(username=username, password=password)
        if user:
            # 用户名密码正确

            login(request, user)

            # 获取登录后所要跳转到的地址
            # 默认跳转到首页

            # 跳转到next_url
            response = redirect('/index')  # HttpResponseRedirect

            # 判断是否需要记住用户名
            remember = request.POST.get('remember')

            if remember == 'on':
                # 记住用户名
                response.set_cookie('username', username, max_age=7 * 24 * 3600)
            else:
                response.delete_cookie('username')

            # 返回response
            return response

        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


# /user/logout
class LogoutView(View):
    '''退出登录'''

    def get(self, request):
        '''退出登录'''
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect('/index/')



