from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about page")

def service(request):
    return HttpResponse("this is service page")

def contact(request):
    return HttpResponse("this is contact page")

