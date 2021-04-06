from django.shortcuts import render,HttpResponse
import logging
# Create your views here.
#apis为setting中Logging配置中的loggers
logger = logging.getLogger('apis')
def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

def base(request):
    return render(request, 'base.html')
