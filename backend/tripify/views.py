from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def package(request):
    return render(request, 'package.html')

def vacation(request):
    return render(request, 'vacation.html')