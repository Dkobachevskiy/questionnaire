from django.shortcuts import get_list_or_404, render
from .models import Group, Question


def index(request):
    questions = Question.objects.all
    context = {
        'questions' : questions,
    }
    return render(request, 'index.html', context)    
