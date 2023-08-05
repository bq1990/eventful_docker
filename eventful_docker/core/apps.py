from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "eventful_docker.core"
    verbose_name = _("Core")

    def ready(self):
        try:
            import eventful_docker.core.signals  # noqa: F401
        except ImportError:
            pass
