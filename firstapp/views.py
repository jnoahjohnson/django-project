from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request):
    context = {
        "name": "Noah"
    }

    return render(request, "firstapp/index.html", context)

def darthPageView(request, darth_name):
    outputString = "Welcome Darth " + darth_name.capitalize()
    return HttpResponse(outputString)