from django.contrib import admin
from django.db.models.enums import Choices

from .models import Question,Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'Choice_text')



admin.site.register(Choice)
admin.site.register(Question)