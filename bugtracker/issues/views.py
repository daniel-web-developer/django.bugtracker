from django.shortcuts import render
from django.shortcuts import redirect
from .models import User, Project, Ticket
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import newProjectForm, newTicketForm
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your views here.
def index(request):
    return render(request, 'index/index.html')
    
def tracker(request, profile_id):
    profile = User.objects.get(pk = profile_id)
    return render(request, 'tracker/index.html', {
        "profile": profile,
        "projects": Project.objects.all().filter(author = profile_id)
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
                project.slug = slugify(project.name)
                project.save()
                return redirect('tracker', profile_id)
        else:
            form = newProjectForm()
            return render(request, 'new/project.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')
    
# def project(request, profile_id, )

@login_required
def new_ticket(request, profile_id):
    profile = User.objects.get(pk = profile_id)
    if request.user.id == profile_id:
        if request.method == "POST":
            form = newTicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.author = request.user
                ticket.created_on = timezone.now()
                ticket.slug = slugify(ticket.name)
                ticket.save()
                return redirect('tracker', profile_id)
        else:
            form = newTicketForm()
            return render(request, 'new/ticket.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')
