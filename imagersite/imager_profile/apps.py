from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):

    name = 'imager_profile'
    verbose_name = 'Imager Profile'

    def ready(self):
        import signals.handlers
        ImagerProfile = self.get_model('ImagerProfile')
