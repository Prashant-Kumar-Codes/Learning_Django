from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse('Hello, world. You are at Prashant"s Home Page')
    return render(request, 'app1.html')

def about(request):
    return HttpResponse('Hello, world. You are at Prashant"s About Page')

def contact(request):
    return HttpResponse('Hello, world. You are at Prashant"s Contact Page')

