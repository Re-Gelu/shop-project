from django.conf import settings

def admin_settings(request):
    return {'ADMIN_SETTINGS': settings.ADMIN_SETTINGS}
