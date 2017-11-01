from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting_view(request):
    return render(request, "greeting.html")

def goodby_view(request):
    return HttpResponse("Goodbye!")

def bmicalc(request):
    pass
    return render(request, "greeting.html")
