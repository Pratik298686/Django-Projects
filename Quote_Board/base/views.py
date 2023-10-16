from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote

# Create your views here.

def quote(request):
    content = Quote.objects.all()
    return render(request,'base/quotes.html',{'content':content})
