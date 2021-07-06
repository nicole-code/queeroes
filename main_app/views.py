from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Queero

# Define the home view
def home(request):
    return HttpResponse('<h1>Thats So Gay</h1>')

def about(request):
    return render(request, 'about.html')

def queero_index(request):
    queero = Queero.objects.all()
    return render(request, 'index.html', {'queeroes': queero})

def queero_detail(request, queero_id):
    queero = Queero.objects.get(id=queero_id)
    return render(request, 'queeroes.html', {'queeroes' : queero})  





