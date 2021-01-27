"""
tnnt template settings
"""

from django.conf import settings


def tnnt_settings(request):
    return_value = dict()

    try:
        return_value[
            "TNNT_TEMPLATE_URLS_TNNT_WEBSITES"
        ] = settings.TNNT_TEMPLATE_URLS_TNNT_WEBSITES
    except AttributeError:
        pass

    try:
        return_value[
            "TNNT_TEMPLATE_URLS_OTHER_WEBSITES"
        ] = settings.TNNT_TEMPLATE_URLS_OTHER_WEBSITES
    except AttributeError:
        pass

    return return_value
