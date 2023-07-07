from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index/index.html')
    
def tracker(request, profile_id):
    profile = User.objects.get(pk = profile_id)
    return render(request, 'tracker/index.html', {
        "profile": profile
    })

def profile(request, profile_id):
    profile = User.objects.get(pk = profile_id)
    return render(request, 'profile/index.html', {
        "profile": profile
    })

@login_required
def new_project(request, profile_id):
    profile = User.objects.get(pk = profile_id)
    if request.user.id == profile_id:
        return render(request, 'new/project.html', {
            "profile": profile
        })
    else:
        return render(request, 'registration/access_denied.html')


# def new_ticket(request, profile_id):
#     profile = User.objects.get(pk = profile_id)
#     return render(request, 'new/ticket.html', {
#         "profile": profile
#     })
