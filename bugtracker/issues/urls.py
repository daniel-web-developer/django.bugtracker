from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:profile_id>/tracker/', views.tracker, name="tracker"),
    path('<int:profile_id>/', views.profile, name="profile-index"),
    path('<int:profile_id>/new_project/', views.new_project, name="new-project"),
]
