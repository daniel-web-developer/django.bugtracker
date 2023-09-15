from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tracker/<int:profile_id>/', views.tracker, name="tracker"),
    path('<int:profile_id>/', views.profile, name="profile-index"),
    path('new_project/<int:profile_id>/', views.new_project, name="new-project"),
    path('new_ticket/<int:profile_id>/<project_link>/', views.new_ticket, name="new-ticket"),
    path('tracker/<int:profile_id>/<project_link>', views.project, name="project"),
    path('tracker/<int:profile_id>/<project_link>/<ticket_link>/', views.ticket, name="ticket"),
    path('tracker/<int:profile_id>/<project_link>/<ticket_link>/edit_ticket', views.edit_ticket, name="edit-ticket")
]
