from django.apps import AppConfig


class ProfileAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_app'


    def ready(self):
        import profile_app.signal.registeruser
        import profile_app.signal.image_delete_user_os