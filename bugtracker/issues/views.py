from django.shortcuts import render
from django.shortcuts import redirect
from .models import User

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
