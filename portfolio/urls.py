from django.urls import path
from .views import list_projects, project_detail

app_name = "projects"

urlpatterns = [
    path("", view=list_projects, name="project_list"),
    path("<slug:project_slug>/", view=project_detail, name="project_detail"),
]
