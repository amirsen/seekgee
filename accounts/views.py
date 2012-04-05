from django.contrib.auth.models import User
from accounts.models import Profile
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def profile(request):
    user = request.user
    try:
        profile = user.get_profile()
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)
    questions_number = profile.questions_number
    return render_to_response('accounts/profile.html', {'user': user, 'questions_number': questions_number})
