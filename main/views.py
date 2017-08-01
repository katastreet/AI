from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question
from django.utils import timezone
from . import firs
import random

# Create your views here.


def index(request):
    lastestQuestionList = Question.objects.order_by('-date')[:5]
    context = {
            'questions': lastestQuestionList,
            }
    return render(request, 'main/index.html', context)


def addToModel(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        # your tensorflow code here
        answer = firs.main(random.randint(0, 5), random.randint(0, 5))
        q = Question(question=question, answer=answer, date=timezone.now())
        q.save()

        answerslist = []
        answerslist += [int(answer)]

        data = {
            "answer": [answerslist],
        }

        return JsonResponse(data)

    return HttpResponse("not for direct call")
