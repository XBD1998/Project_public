import logging
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import UserLog
import time
#当请求完成后打印一个日志
@receiver(request_finished)
def all_log(sender, **kwargs):
    print(sender, kwargs)
    print("使用信号记日志")

#当创建一条记录MailLog之后，会自动执行发送邮件
"""
@receiver(post_save, sender=MailLog)
def send_mail(sender, instance, **kwargs):
    pass
"""
@receiver(post_save, sender=UserLog)
def send_mail(sender, instance, **kwargs):
    print(sender, instance, kwargs)
    # time.sleep(20)
    print("XXX发送的信号")

