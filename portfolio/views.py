from django.shortcuts import render

def index(request):
    return render(request,'portfolio/index.html')

def introduction(request):
    return render(request,'portfolio/introduction.html')