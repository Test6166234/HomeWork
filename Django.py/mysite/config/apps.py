from django.apps import AppConfig
from django.contrib import admin


class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text')