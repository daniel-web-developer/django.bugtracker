from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tracker/<int:profile_id>', views.tracker, name="tracker"),
    path('<int:profile_id>', views.profile, name="profile-index"),
    path('new_project/<int:profile_id>', views.new_project, name="new-project"),
]
