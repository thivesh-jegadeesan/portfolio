from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    # template = loader.get_template('home/index.html')
    # return HttpResponse(template.render())
    return render(request, 'home/index.html')

def about(request):
    # template = loader.get_template('about/index.html')
    # return HttpResponse(template.render())
    return render(request, 'about/index.html')

def resume(request):
    template = loader.get_template('resume/index.html')
    return HttpResponse(template.render())
    # return render(request, 'resume/index.html')

def skills(request):
    # template = loader.get_template('skills/index.html')
    # return HttpResponse(template.render())
    return render(request, 'skills/index.html')

def contact(request):
    template = loader.get_template('contact/index.html')
    return HttpResponse(template.render())
    # return render(request, 'contact/index.html')

def resume(request):
    template = loader.get_template('resume/index.html')
    return HttpResponse(template.render())
    # return render(request, 'contact/index.html')
    
def project(request):
    # template = loader.get_template('skills/index.html')
    # return HttpResponse(template.render())
    return render(request, 'projects/index.html')