from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^$', views.index, name='index'),
    #题目列表
    # url(r'^questions/$', TemplateView.as_view(template_name="questions.html"), name="questions"),
    url(r'^questions/$', views.QuestionsList.as_view(),name="questions"),
    #贡献题目
    url(r'^question/$', views.test, name="question"),
    #题目详情， 捕获了一个参数
    url(r'^question/id/$', TemplateView.as_view(template_name="question_detail.html"),name="question_detail"),
]