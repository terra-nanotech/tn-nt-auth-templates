from django.conf import settings

default_app_config = "tnnt_templates.apps.TnntTemplatesConfig"

__version__ = "1.4.1"
__title__ = "{entity_name} Template Overrides".format(
    entity_name=settings.TNNT_TEMPLATE_ENTITY_NAME
)
