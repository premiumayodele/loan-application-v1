from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('This will be the homepage')

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def about(request):
    template_name = 'about.html'
    return render(request, template_name)

def team(request):
    template_name = 'team.html'
    return render(request, template_name)

def products(request):
    template_name = 'products.html'
    return render(request, template_name)

def personal(request):
    template_name = 'loan/personal.html'
    return render(request, template_name)

def home(request):
    template_name = 'loan/home.html'
    return render(request, template_name)

def education(request):
    template_name = 'loan/education.html'
    return render(request, template_name)

def business(request):
    template_name = 'loan/business.html'
    return render(request, template_name)

def car(request):
    template_name = 'loan/car.html'
    return render(request, template_name)

def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)

def blog(request):
    template_name = 'blog.html'
    return render(request, template_name)