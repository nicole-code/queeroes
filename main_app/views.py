from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from .models import Queero, Quotes, Community

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    q = Queero.objects.get(id=1)
    c = Community.objects.get(id=1)
    q.Community.add(c)
    
    return render(request, 'about.html')

def queero_index(request):
    queero = Queero.objects.all()
    return render(request, 'index.html', {'queeroes': queero})

def queero_detail(request, queero_id):
    queero = Queero.objects.get(id=queero_id)
    quote = queero.quotes_set.all()
    return render(request, 'queeroes.html', {'queeroes' : queero , 'quotes': quote})  

def queero_new(request):
    return render(request, 'new.html')    

def queero_create(request):
    queero = Queero.objects.create(
        name=request.POST['name'],
        occupation=request.POST['occupation'],
        biography=request.POST['biography'],
        legacy=request.POST['legacy'],
    )
    return redirect(f'/queeroes/{queero.id}')

def queero_delete(request, queero_id):
    queero = Queero.objects.get(id=queero_id)    
    queero.delete()
    return redirect('/index')

def queero_edit(request, queero_id):
    queero = Queero.objects.get(id=queero_id)  
    return render(request, 'edit.html', {'queeroes' : queero}) 

def queero_update(request, queero_id):    
    queero = Queero.objects.get(id=queero_id)  
    queero.name = request.POST['name']
    queero.occupation = request.POST['occupation']
    queero.biography = request.POST['biography']
    queero.legacy= request.POST['legacy']
    queero.save()
    return redirect(f'/queeroes/{queero.id}')

def add_queero_quote(request, queero_id):
    queero = Queero.objects.get(id=queero_id)
    Quotes.objects.create(
        quote=request.POST['quote'],
        queero_id=queero_id,
    )
    return redirect(f'/queeroes/{queero.id}')