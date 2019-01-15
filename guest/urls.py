from django.conf.urls import url,include
from django.contrib import admin
from sign.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls', namespace='user')),  # 用户模块 路由
    url(r'^sign/', include('sign.urls',namespace='sign')),  # 签到模块 路由

    url(r'^', index),

]
