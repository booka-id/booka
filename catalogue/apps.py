from django.apps import AppConfig


class CatalogueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogue'
    
    # def ready(self):
    #     from django.core import management
    #     management.call_command('set_initial_stock')