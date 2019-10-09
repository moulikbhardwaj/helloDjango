from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from .models import Question, Choice
from django.urls import reverse

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
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{'question':question, 'error_message':'You did\'nt selected a choice'})
	else:
		selected_choic.vote+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))