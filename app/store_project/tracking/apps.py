from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrackingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_project.tracking'
    verbose_name = _("Tracking")
