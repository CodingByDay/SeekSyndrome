from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Project, Image, New, NewsPicture

# Create your views here.



#
def home(request):
    return render(request, 'main/index.html', {})

#
def about(request):
    project = New.objects.all()
    picture = NewsPicture.objects.all()
    
    context = {
        "news_list": project,
        "picture_list": picture       
    }
    
    return render(request, 'main/about.html', context)    


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
    pictures = Image.objects.filter(product=id)
    # Getting the information to the view itself.
    
    context = {
        "project": object,
        "id": id,
        "pictures": pictures
    }
    
    
    return render(request, 'main/specific.html', context)
     

# News view



def news(request, id):
    object = New.objects.get(id=id)
    pictures = NewsPicture.objects.filter(product=id)
    
    context = {
        "news": object,
        "id": id,
        "pictures": pictures
    }
    
    
    return render(request, 'main/news.html', context)
