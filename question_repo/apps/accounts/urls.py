from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
#CBV => class base view
#FBV => function base view
urlpatterns = [
    #TemplateView可以不写视图函数
    # url(r'^register/$', TemplateView.as_view(template_name="accounts/register.html"), name="register"),
    # 注册
    url(r'register/$', views.Register.as_view(), name="register"),
    # 登录
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name="login"),
    # url(r'login/$', views.test, name="login"),
    # 退出
    url(r'logout/$', views.test, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.test, name="password_forget"),
    # 重置密码
    url(r'password/reset/token/$', views.test, name="password_reset"),
]
