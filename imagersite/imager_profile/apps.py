from django.apps import AppConfig

class ImagerProfileConfig(AppConfig):
    def ready(self):
        ImagerProfile = self.get_model('ImagerProfile')
        # import signals module