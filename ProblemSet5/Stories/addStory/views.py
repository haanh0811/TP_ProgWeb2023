from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django import forms
from .models import Author, Quotes, QuotesForm
import uuid

# Create your views here.


def homepage(request):
    #return render(request, 'addStory/homepage.html',{
        #'qsets' : Quotes.objects.all()
        
    #})
    quotes = Quotes.objects.all()
    return render(request, 'addStory/homepage.html', {'quotes': quotes})

def add(request):
    #global id
    if request.method == 'POST':
        #form = NewStory(request.POST)
        form = QuotesForm(request.POST)
        if form.is_valid():
           form.save()
           #id +=1
           return redirect('homepage')
    else:
        form = QuotesForm()
    return render(request, 'addStory/add.html', {'form': form})



def entry(request, id):
    try:
        quote = Quotes.objects.get(id=id)
        return JsonResponse({'id': quote.id, 'quote': quote.quote, 'author' : str(quote.author)})
    except Quotes.DoesNotExist():
        return JsonResponse({'error': 'Quote not found'})

