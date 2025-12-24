from django.shortcuts import render

def index(request):
    return render(request, 'res_app/index.html')

def menu(request):
    return render(request, 'res_app/menu.html')

def about(request):
    return render(request, 'res_app/about.html')

def contact(request):
    return render(request, 'res_app/contact.html')

# Create your views here.
