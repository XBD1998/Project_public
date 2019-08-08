from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mobile_captcha/$',views.mobile_captcha,name='mobile_captcha'),
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    url(r'^questions/$', views.QuestionsView.as_view(), name='questions')
]
