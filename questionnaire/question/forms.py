from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        labels = {'text': 'Текст ответа'}

form = QuestionForm()
