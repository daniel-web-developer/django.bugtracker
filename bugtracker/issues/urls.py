from django.urls import path

from . import views
from .views import search

urlpatterns = [
    path('', views.index, name="index"),
    path('tracker/<int:profile_id>/', views.tracker, name="tracker"),
    path('<int:profile_id>/', views.profile, name="profile-index"),
    path('tracker/<int:profile_id>/<project_link>/', views.project, name="project"),
    path('new_project/<int:profile_id>/', views.new_project, name="new-project"),
    path('tracker/<int:profile_id>/<project_link>/edit_project', views.edit_project, name="edit-project"),
    path('tracker/<int:profile_id>/<project_link>/delete_project', views.delete_project, name="delete-project"),
    path('new_ticket/<int:profile_id>/<project_link>/', views.new_ticket, name="new-ticket"),
    path('tracker/<int:profile_id>/<project_link>/<ticket_link>/', views.ticket, name="ticket"),
    path('tracker/<int:profile_id>/<project_link>/<ticket_link>/edit_ticket', views.edit_ticket, name="edit-ticket"),
    path('tracker/<int:profile_id>/<project_link>/<ticket_link>/delete_ticket', views.delete_ticket, name="delete-ticket"),
    path('tracker/<int:profile_id>/<project_link>/search/', views.search, name="search"),
    path('accounts/register', views.register, name="register"),
]
