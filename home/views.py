from urllib import response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        project = request.POST.get('project')
        Description = request.POST.get('desc')
        contact = Contact(name=name, email=email, project=project, Description=Description)
        contact.save()

    return render(request,'index.html')


