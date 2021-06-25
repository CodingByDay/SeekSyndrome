from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Project, Image

# Create your views here.



#
def home(request):
    return render(request, 'main/index.html', {})

#
def about(request):
    return render(request, 'main/about.html', {})    


def project(request):
    project = Project.objects.all()
    picture = Image.objects.all()
    
    context = {
        "project_list": project,
        "picture_list": picture       
    }
    
    return render(request, 'main/project.html', context)        


     
