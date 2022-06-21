from django.apps import AppConfig


class PublicationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'publication_app'

    def ready(self):
        import signals.image_delete_editpost_os
        import signals.image_delete_post_os
