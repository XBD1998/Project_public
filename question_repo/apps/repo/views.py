from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("题库视图")

