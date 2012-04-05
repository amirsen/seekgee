from qaa.models import Question, Answer, Category
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

def index(request):
    latest_questions = Question.objects.all().order_by('-pub_date')[:5]
    return render_to_response('qaa/index.html', {'latest_questions': latest_questions}, context_instance=RequestContext(request))

def ask(request):
    question_title = request.POST['question_title']
    category_list = Category.objects.all()
    return render_to_response('qaa/ask.html', {'question_title': question_title,
                                               'category_list': category_list}, context_instance=RequestContext(request))

def submit(request):
    question_title = request.POST['title']
    question_desc = request.POST['description']
    category = Category.objects.get(pk=int(request.POST['category']))
    if ( not question_title ) or ( not question_desc ):
        error_message = 'You must fill all fields.'
        return render_to_response('qaa/ask.html', {'question_title': '',
                                            'error_message': error_message},
                           context_instance=RequestContext(request))
    else:
        q = Question.objects.create(title=question_title, desc=question_desc, pub_date=datetime.datetime.now(), category=category)
        return HttpResponseRedirect(reverse('qaa.views.index'))
