from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import RegisterView,  LoginView, LogoutView

urlpatterns = [

    url(r'^register$', RegisterView.as_view(), name='register'), # 注册


   url(r'^login$', LoginView.as_view(), name='login'), # 登录
   url(r'^logout$', LogoutView.as_view(), name='logout'), # 注销登录



]