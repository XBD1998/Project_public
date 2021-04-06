from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    html = "<h1>我是来自route_resolve的路由</h1>"
    return HttpResponse(html)