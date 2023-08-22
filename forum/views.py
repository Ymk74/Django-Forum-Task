from django.shortcuts import render
from .models import Question , Answer
# Create your views here.

def question_list(request):
    data = Question.objects.all()
    return render(request, 'forum/list.html',{'data':data})
    