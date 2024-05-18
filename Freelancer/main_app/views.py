from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile

def index (request) :
    return render (request , 'index.html')

def profile (request , id) :
     if request.method == "GET": 
        info = Profile.objects.get(id = id)
        return JsonResponse(info.serialize())
   