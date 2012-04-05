from qaa.models import Question
from accounts.models import Profile
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    latest_questions = Question.objects.all().order_by('-pub_date')[:5]
    most_active_profiles = Profile.objects.all().order_by('questions_number')[:5]
    return render_to_response('main/index.html', {'latest_questions': latest_questions, 'most_active_profiles': most_active_profiles}, context_instance=RequestContext(request))
