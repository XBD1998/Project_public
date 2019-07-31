from django.shortcuts import render
from django.shortcuts import HttpResponse

def test(request):
    return HttpResponse("个人中心视图")
# Create your views here.
