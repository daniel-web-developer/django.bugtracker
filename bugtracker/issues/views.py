from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import newProjectForm
from django.utils import timezone
from django.template.defaultfilters import slugify


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
        if request.method == "POST":
            form = newProjectForm(request.POST)
            if form.is_valid():
                project = form.save(commit=False)
                project.author = request.user
                project.created_on = timezone.now()
                project.save()
                project.slug = slugify(project.name)
                return(redirect('tracker', profile.id))
        else:
            form = newProjectForm()
            return render(request, 'new/project.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')


# def new_ticket(request, profile_id):
#     profile = User.objects.get(pk = profile_id)
#     return render(request, 'new/ticket.html', {
#         "profile": profile
#     })
