from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
#CBV => class base view
#FBV => function base view
urlpatterns = [
    #TemplateView���Բ�д��ͼ����
    # url(r'^register/$', TemplateView.as_view(template_name="accounts/register.html"), name="register"),
    # ע��
    url(r'register/$', views.Register.as_view(), name="register"),
    # ��¼
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name="login"),
    # url(r'login/$', views.test, name="login"),
    # �˳�
    url(r'logout/$', views.test, name="logout"),
    # ��������
    url(r'password/forget/$', views.test, name="password_forget"),
    # ��������
    url(r'password/reset/token/$', views.test, name="password_reset"),
]
