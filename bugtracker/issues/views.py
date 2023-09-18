from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Project, Ticket
from django.contrib.auth.decorators import login_required
from .forms import newProjectForm, newTicketForm, editTicketForm
from django.utils import timezone
import secrets
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def generate_permalink(newObject):
    while (True):
        permalink = secrets.token_urlsafe(10)[:10]
        if newObject.objects.filter(permalink = permalink).count() == 0:
            break
    return permalink


def index(request):
    return render(request, 'index/index.html')
    
def tracker(request, profile_id):
    profile = get_object_or_404(User, pk = profile_id)
    return render(request, 'tracker/index.html', {
        "profile": profile,
        "projects": Project.objects.all().filter(author = profile_id)
    })

def project(request, profile_id, project_link):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, permalink = project_link)
    if request.method == "GET":
        query = request.GET.get("q", '')
        if query == None:
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
        else:
            if projectid.public == 1:
                return render(request, 'tracker/projects.html', {
                    "profile": profile,
                    "projects": Project.objects.all().filter(author = profile_id),
                    "theproject": projectid,
                    "tickets": Ticket.objects.all().filter(title__contains=query)
                    })
            else:
                if request.user.id == profile.id:
                    return render(request, 'tracker/projects.html', {
                        "profile": profile,
                        "projects": Project.objects.all().filter(author = profile_id),
                        "theproject": projectid,
                        "tickets": Ticket.objects.all().filter(title__conaints=query)
                        })
                else:
                    return render(request, 'registration/access_denied.html')
    else:
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

#class search(ListView):
 #   model = Ticket
  #  template_name = 'tracker/projects.html'

   # def get_queryset(self):
    #    query = self.request.GET.get("q")
    #    return Ticket.objects.filter(Q(title__icontains=query))

def search(request, profile_id, project_link):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, permalink = project_link)
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


def ticket(request, profile_id, project_link, ticket_link):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, permalink = project_link)
    ticketid = get_object_or_404(Ticket, permalink = ticket_link)
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
                project.permalink = generate_permalink(Project)
                project.save()
                return redirect('project', profile_id, project.permalink)
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

def new_ticket(request, profile_id, project_link):
    profile = get_object_or_404(User, pk = profile_id)
    project = get_object_or_404(Project, permalink = project_link)
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
                ticket.permalink = generate_permalink(Ticket)
                ticket.save()
                return redirect('project', profile.id, project.permalink)
        else:
            form = newTicketForm()
            return render(request, 'new/ticket.html', {
                "profile": profile,
                "form": form
            })
    else:
        return render(request, 'registration/access_denied.html')

@login_required
def edit_ticket(request, profile_id, project_link, ticket_link):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, permalink = project_link)
    ticketid = get_object_or_404(Ticket, permalink = ticket_link)
    if request.user.id == profile_id:
        if request.method == "POST":
            form = editTicketForm(request.POST, instance=ticketid)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.author = request.user
                ticket.created_on = ticket.created_on
                ticket.edited_on = timezone.now()
                ticket.project = projectid
                ticket.permalink = ticket.permalink
                ticket.save()
                return redirect('ticket', profile.id, projectid.permalink, ticketid.permalink)
            else:
                return render(request, 'registration/access_denied.html')
        else:
            form = editTicketForm(instance=ticketid)
            return render(request, 'edit/ticket.html', {'form': form})
    else:
        return render(request, 'registration/access_denied.html')

def delete_ticket(request, profile_id, project_link, ticket_link):
    profile = get_object_or_404(User, pk = profile_id)
    projectid = get_object_or_404(Project, permalink = project_link)
    ticketid = get_object_or_404(Ticket, permalink = ticket_link)
    if request.user.id == profile.id:
        try:
            ticketid.delete();
            return render(request, 'tracker/delete.html', {
                "profile": profile,
                "project": projectid, 
                })
        except Exception:
            return HttpResponse("Something went wrong.")
    else:
        return render(request, 'registration/access_denied.html')

