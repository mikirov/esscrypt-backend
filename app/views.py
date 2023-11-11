from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'app/project_list.html', {'projects': projects})

def main_page(request):
    return render(request, 'app/main.html')