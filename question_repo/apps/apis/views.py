from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from libs import sms
import random
from django.core.cache import cache
import logging
logger = logging.getLogger('apis')
from  io import BytesIO
from libs import patcha
import base64
from django.views.generic import View
from apps.repo.models import Questions
# Create your views here.
def mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        # 将短信验证码写入redis, 300s 过期
        cache.set(mobile, mobile_captcha, 300)
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "验证码发送失败！"}
    return JsonResponse(ret)

def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = patcha.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type+base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)

def check_captcha(request):
    ret = {"code":400, "msg":"验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code', "")
    session_captcha_code = request.session.get('captcha_code', "")
    print(post_captcha_code, session_captcha_code)
    if post_captcha_code and post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
    return JsonResponse(ret)


# class QuestionsView(LoginRequiredMixin, View):
#     def get(self, request):
#         """
#         :param request:
#         :return:
#         """
#         # 获取参数
#         pagesize = int(request.GET.get("limit", 10))
#         offset = int(request.GET.get("offset", 0))
#         page = int(request.GET.get("page", 1))
#         grade = int(request.GET.get("grade", 0))
#         status = int(request.GET.get("status", 2))
#         # 2: 不筛选， 1，已刷，0，待刷
#         category = int(request.GET.get("category", 0))
#
#         # 取出所有数据，筛选指定等级和分类
#         # questions_list = Questions.objects.all()
#         questions_list = Questions.objects.filter(status=True)
#         # if search:
#         #     questions_list = questions_list.filter(title__icontains=search)
#
#         if search:
#             if search.isdigit():
#                 questions_list = questions_list.filter(
#                     Q(id=search) | Q(content__icontains=search) | Q(title__icontains=search))
#             else:
#                 questions_list = questions_list.filter(Q(content__icontains=search) | Q(title__icontains=search))
#
#     if grade: questions_list = questions_list.filter(grade=grade)
#     if category: questions_list = questions_list.filter(category__id=category)
#
#     # 筛选状态 => 我的答题表
#
#     questions_list = questions_list.values('id', 'title', 'grade', 'answer')
#     total = len(questions_list)
#
#     # 计算当前页面的数据
#     questions_list = questions_list[offset:offset + pagesize]
#     print(type(questions_list))
#     print(questions_list)
#     # 用于计算当前登录的用户是否收藏对应的题目，如果收藏实心True，没有收藏空心False
#     for item in questions_list:
#         item["collection"] = True if QuestionsCollection.objects.filter(
#             user=request.user, status=True, question_id=item["id"]) else False
#     questions_dict = {'total': total, 'rows': list(questions_list)}
#     return JsonResponse(questions_dict)
#     questions_list = Questions.objects.all()
#     # questions_list = Questions.objects.filter(status=True)
#
#     if grade: questions_list = questions_list.filter(grade=grade)
#     if category: questions_list = questions_list.filter(category__id=category)
#     # func2
#     questions_list = list(questions_list.values('id', 'title', 'grade', 'answer'))
#
#     total = len(questions_list)
#     questions_list = questions_list[offset:offset + pagesize]
#
#     # 格式是bootstrap-table要求的格式
#     questions_dict = {'total': total, 'rows': questions_list}
#     return JsonResponse(questions_dict, safe=False)

from django.http import JsonResponse
from django.views.generic import View
from apps.repo.models import Questions
from django.db.models import Q

class QuestionsView(View):
    def get(self, request):
        """
        :param request:
        :return:
        # /apis/questions/?order=asc&offset=0&limit=25
        # /apis/questions/?pagesize=25&offset=0&page=1&grade=4&category=1&status=1
        """
        # 获取参数
        page = int(request.GET.get("page", 1))
        pagesize = int(request.GET.get("pagesize", 25))
        offset = int(request.GET.get("offset", 0))
        grade = int(request.GET.get("grade",0))
        category = int(request.GET.get("category",0))
        # 2: 不筛选， 1，已刷，0，待刷
        status = int(request.GET.get("status", 0))

        # 取出所有数据，筛选指定等级和分类
        questions_list = Questions.objects.filter(status=1)
        # if search:
        #     questions_list = questions_list.filter(title__icontains=search)
        search = ""
        if search:
            if search.isdigit():
                questions_list = questions_list.filter(
                    Q(id=search) | Q(content__icontains=search) | Q(title__icontains=search))
            else:
                questions_list = questions_list.filter(Q(content__icontains=search) | Q(title__icontains=search))

        if grade: questions_list = questions_list.filter(grade=grade)
        if category: questions_list = questions_list.filter(category__id=category)

        # 筛选状态 => 我的答题表
        questions_list = questions_list.values('id', 'title', 'grade', 'answer')
        total = len(questions_list)

        # 计算当前页面的数据
        questions_list = questions_list[offset:offset + pagesize]

        # 用于计算当前登录的用户是否收藏对应的题目，如果收藏实心True，没有收藏空心False
        # for item in questions_list:
        #     item["collection"] = True if QuestionsCollection.objects.filter(
        #         user=request.user, status=True, question_id=item["id"]) else False

        # 格式是bootstrap-table要求的格式
        questions_dict = {'total': total, 'rows': list(questions_list)}
        return JsonResponse(questions_dict)

