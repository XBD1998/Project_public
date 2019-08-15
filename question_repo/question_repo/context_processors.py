from . import settings

def site_info(request):
    #站点基本信息
    site = {}
    site["SITE_NAME"] = settings.SITE_NAME
    site["SITE_DESC"] = settings.SITE_DESC
    site["SITE_LOCAL"] = settings.SITE_LOCAL
