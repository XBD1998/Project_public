from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^mobile_captcha/$',views.mobile_captcha,name='mobile_captcha')
]
