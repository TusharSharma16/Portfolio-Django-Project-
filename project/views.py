from django.shortcuts import render

from .models import Project

def allprojects(request):
    project = Project.objects
    return render(request, 'project/allprojects.html', {'project':project})
