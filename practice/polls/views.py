from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def results(request: HttpRequest, question_id) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request: HttpRequest, question_id) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)