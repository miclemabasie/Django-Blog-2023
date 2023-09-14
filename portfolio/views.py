from django.shortcuts import render, get_object_or_404
from .models import Portfolio


def list_projects(request):
    # List out the diffent available projects
    projects = Portfolio.objects.filter(is_active=True)
    template_name = "portfolio/list.html"
    context = {
        "works": projects,
    }
    return render(request, template_name, context)


def project_detail(request, project_slug):
    project = get_object_or_404(Portfolio, slug=project_slug)
    template_name = "portfolio/detail.html"
    context = {
        "project": project,
    }

    return render(request, template_name, context)
