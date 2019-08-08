from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Questions
# Create your views here.
def test(request):
    return HttpResponse("题库视图")

# class Index(View):
#     def get(self, request):

#需要用户登录了才能访问该页面，如果没有登录，跳转到 =》 'accounts.login.html'
@login_required
def index(request):
    return render(request, "accounts/index.html")


class QuestionsList(View):
    def get(self, request):
        category = Category.objects.all().values("id", "name")
        grades = Questions.DIF_CHOICES
        kwgs = {"category":category, "grades":grades}
        return render(request, 'questions.html', kwgs)