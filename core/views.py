from django.shortcuts import render
from django.http import HttpResponse
from core.forms import BMIForm

# Create your views here.

def greeting_view(request):
    return render(request, "greeting.html")

def goodby_view(request):
    return HttpResponse("Goodbye!")

def bmi(request):
    if request.method == "POST"
    form = BMIForm()
    return render(request, "bmicalc.html", {"form": form})
