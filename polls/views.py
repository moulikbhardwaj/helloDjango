from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	output = '<br>'.join([q.question_text for q in latest_question_list])
	return render(request,'polls/index.html', {"latest_question_list":latest_question_list})

def details(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question doesnot exist")
	return render(request, 'polls/details.html',{'question':question})

def results(request, question_id):
	return HttpResponse('You are looking at results of question {}'.format(question_id))

def vote(request, question_id):
	return HttpResponse('You are voting on question {}'.format(question_id))
