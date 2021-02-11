from django.apps import AppConfig
from django.conf import settings
from . import __version__


class TnntTemplatesConfig(AppConfig):
    name = "tnnt_templates"
    label = "tnnt_templates"
    verbose_name = "{entity_name} Auth Templates v{version}".format(
        entity_name=settings.TNNT_TEMPLATE_ENTITY_TYPE, version=__version__
    )
