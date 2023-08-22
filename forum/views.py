from django.shortcuts import render
from .models import Question , Answer
# Create your views here.

def question_list(request):
    data = Question.objects.all()
    return render(request, 'forum/list.html',{'data':data})
    

def question_detail(request ,id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'forum/detail.html',{'data':question , 'answers':answers})
    