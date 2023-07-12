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

def project(request, profile_id, project_id):
    profile = User.objects.get(pk = profile_id)
    projectid = Project.objects.get(pk = project_id)
    # project = Project.objects.all().filter(pk = project_id)
    # add function to stop unauthorised users from accessing page
        
    return render(request, 'tracker/projects.html', {
        "profile": profile,
        "projects": Project.objects.all().filter(author = profile_id),
        "theproject": projectid,
        "tickets": Ticket.objects.all().filter(project = projectid)
    })

def ticket(request, profile_id, project_id, ticket_id):
    profile = User.objects.get(pk = profile_id)
    projectid = Project.objects.get(pk = project_id)
    ticketid = Ticket.objects.get(pk = project_id)
    return render(request, 'tracker/projects.html', {
        "profile": profile,
        "projects": Project.objects.all().filter(author = profile_id),
        "theproject": projectid,
        "tickets": Ticket.objects.all()
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
                # return redirect('tracker', profile_id)
                return redirect('project', profile_id, project.id)
            else:
                return render(request, 'new/project.html', {
                    "profile": profile,
                    "form": form
                })
        else:
            form = newProjectForm()
            return render(request, 'new/project.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')

@login_required
def new_ticket(request, profile_id, project_id):
    profile = User.objects.get(pk = profile_id)
    project = Project.objects.get(pk = project_id)
    if request.user.id == profile_id:
        if request.method == "POST":
            form = newTicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.author = request.user
                ticket.created_on = timezone.now()
                ticket.project = project
                ticket.slug = slugify(ticket.title)
                ticket.save()
                return render(request, 'tracker/projects.html', {
                    "profile": profile,
                    "projects": Project.objects.all().filter(author = profile_id),
                    "theproject": Project.objects.get(pk = project_id),
                    "tickets": Ticket.objects.all().filter(project = profile_id)
                })
                # return redirect('project', profile_id)
        else:
            form = newTicketForm()
            return render(request, 'new/ticket.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')
