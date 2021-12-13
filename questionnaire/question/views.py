from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from .models import Group, Question


def index(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }
    return render(request, 'index.html', context)    

def new_answer(request):
    form = PostForm(request.POST, files=request.FILES or None)
    if request.method != 'POST':
        return render(request, 'index.html', {'form':form})
    if form.is_valid():
        post_get = form.save(commit=False)
        post_get.save()
        return redirect('thanks')
    return render(request, 'new.html', {'form':form})

def showthanks(request):
    message = 'Thanks for your answer'
    context = {
        'thanks' : message
    }
    return render(request, 'thanks.html', context)
