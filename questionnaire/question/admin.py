from django.contrib import admin

from .models import Answer, Group, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'pub_date', 'group')
    search_fields = ('group',)
    empty_value_display = '-пусто-'

admin.site.register(Question, QuestionAdmin)
admin.site.register(Group)
admin.site.register(Answer)

