from django.shortcuts import render, HttpResponse

# Create your views here.

def dashboard(request):
    template_name = 'products/dashboard.html'
    return render(request, template_name)

def apply(request):
    template_name = 'products/apply.html'
    return render(request, template_name)