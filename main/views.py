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

   
# Specific project view
def specific(request, id):
    object = Project.objects.get(id=id)
    
    # Getting the information to the view itself.
    
    context = {
        "project": object
    }
    
    
    return render(request, 'main/specific.html', context)
     
