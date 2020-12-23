from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'MainApp/home.html')

def memories(request):
    return render(request, 'MainApp/memories.html')
