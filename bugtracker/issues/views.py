from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Project, Ticket
from django.contrib.auth.decorators import login_required
from .forms import newProjectForm, newTicketForm, editTicketForm
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your views here.
def index(request):
    return render(request, 'index/index.html')
    
def tracker(request, profile_id):
    profile = get_object_or_404(User, pk = profile_id)
    return render(request, 'tracker/index.html', {
        "profile": profile,
        "projects": Project.objects.all().filter(author = profile_id)
    })

def project(request, profile_id, project_id):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, pk = project_id)
    # project = Project.objects.all().filter(pk = project_id)
    if projectid.public == 1:
        return render(request, 'tracker/projects.html', {
                "profile": profile,
                "projects": Project.objects.all().filter(author = profile_id),
                "theproject": projectid,
                "tickets": Ticket.objects.all().filter(project = projectid)
            })
    else:
        if request.user.id == profile.id:
            return render(request, 'tracker/projects.html', {
                "profile": profile,
                "projects": Project.objects.all().filter(author = profile_id),
                "theproject": projectid,
                "tickets": Ticket.objects.all().filter(project = projectid)
            })
        else:
            return render(request, 'registration/access_denied.html')

def ticket(request, profile_id, project_id, ticket_id):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, pk = project_id)
    ticketid = get_object_or_404(Ticket, pk = ticket_id)
    if ticketid.public == 1 and projectid.public == 1:
        return render(request, 'tracker/ticket.html', {
            "profile": profile,
            "projects": Project.objects.all().filter(author = profile_id),
            "project": projectid,
            "ticket": ticketid
        })
    else:
        if request.user.id == profile.id:
            return render(request, 'tracker/ticket.html', {
                "profile": profile,
                "projects": Project.objects.all().filter(author = profile_id),
                "project": projectid,
                "ticket": ticketid
            })
        else:
            return render(request, 'registration/access_denied.html')

def profile(request, profile_id):
    profile = get_object_or_404(User, pk = profile_id)
    return render(request, 'profile/index.html', {
        "profile": profile
    })

@login_required
def new_project(request, profile_id):
    profile = get_object_or_404(User, pk = profile_id)
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

# @login_required
def new_ticket(request, profile_id, project_id):
    profile = get_object_or_404(User, pk = profile_id)
    project = get_object_or_404(Project, pk = project_id)
    if request.user.id == profile_id:
        if request.method == "POST":
            form = newTicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.author = request.user
                ticket.created_on = timezone.now()
                ticket.edited_on = None
                ticket.project = project
                ticket.solved = 0
                ticket.slug = slugify(ticket.title)
                ticket.save()
                return redirect('project', profile.id, project.id)
        else:
            form = newTicketForm()
            return render(request, 'new/ticket.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')

@login_required
def edit_ticket(request, profile_id, project_id, ticket_id):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, pk = project_id)
    ticketid = get_object_or_404(Ticket, pk = ticket_id)
    if request.user.id == profile_id:
        if request.method == "POST":
            form = editTicketForm(request.POST, instance=ticketid)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.author = request.user
                ticket.created_on = ticket.created_on
                ticket.edited_on = timezone.now()
                ticket.project = projectid
                ticket.slug = slugify(ticket.title)
                ticket.save()
                # return render(request, 'tracker/ticket.html', {
                #     "profile": profile,
                #     "projects": Project.objects.all().filter(author = profile_id),
                #     "project": projectid,
                #     "ticket": ticketid
                # })
                return redirect('ticket', profile.id, projectid.id, ticketid.id)
            else:
                return render(request, 'registration/access_denied.html')
        else:
            form = editTicketForm(instance=ticketid)
            return render(request, 'edit/ticket.html', {'form': form})
    else:
        return render(request, 'registration/access_denied.html')
