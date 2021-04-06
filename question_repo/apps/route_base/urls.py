from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'zoos/(\d+)/', views.zoos, name="zoos"),
    #url(regex：正则，view：视图，kwgs：传递给视图的参数，name：为url/视图命名
    #http://localhost:8000/route_base/index/
    #route_base/index/ => 跟regex匹配
    #1.^route_base/ => 剩下index/
    #2.^index/$ => 匹配上了
    #()分组 =》 参数捕获（参数以位置参数方式传递，views.zoos(request, id）
    # url(r'zoos1/(\d+)/', views.zoos1, name="zoos1"),
    # # ()分组 => 参数命名（参数以关键字参数方式传递），views.zoos(request, id=xxx)
    # url(r'^zoos2/(?P<id>\d+)/', views.zoos2, name="zoos2"),
    # #第三个参数，额外传递一个参数type 给视图，views.zoos3(request, id=xx, type=dog)
    # url(r'zoos/(?P<id>\d+)/', views.zoos3, {"type":"dog"}, name="zoos3"),
    # url(r'login/$', views.login, {'status':1}, name="login")
]
"""
注意：
1.除了include包含，建议都要加$
2.注意URL尾部/
3.路由匹配顺序 => 执行第一条匹配上的规则
    /root_base/index/1/
    /zoos/
    /zoos/id/
"""