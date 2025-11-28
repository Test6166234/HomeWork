from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db.models.enums import Choices

from .models import Employees
from .models import Question
from .models import Choices



class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'position', 'salary')
    list_filter = ('position',)
    search_fields = ('name',)



admin.site.register(Employees,EmployeesAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    class ChoiceAdmin(admin.ModelAdmin):
        list_display = ('question_text', 'Choice_text')

admin.site.register(Choices,ChoiceAdmin)



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)









admin.site.register(Question,QuestionAdmin)

