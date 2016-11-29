from django.conf import settings


def all_context(request):
    SITE_NAME = settings.SITE_NAME
    SITE_BLOG_DES = settings.SITE_BLOG_DES
    SITE_URL = settings.SITE_URL
    return locals()
