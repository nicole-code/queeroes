from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Thats So Gay</h1>')

def about(request):
    return render(request, 'about.html')

def queero_index(request):
    return render(request, 'index.html')

# { 'queeroes': queeroes }    





