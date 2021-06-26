from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Order, Project, Image, New, NewsPicture
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm




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



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['jankojovicic351@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/') 


            
    return render(request, 'main/email.html', {'form': form})



def successView(request):
    return HttpResponse('Success! Thank you for your message.')