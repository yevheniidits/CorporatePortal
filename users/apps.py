from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.models