from django.http import HttpResponse
from django.shortcuts import render

def  home(request):
    # return HttpResponse("Hello world. I am learning Django")
    return render(request,'website/home.html')

def  about(request):
    # return HttpResponse("Hello world. This is about page.")
    return render(request,'website/about.html')

def  contact(request):
    # return HttpResponse("Hello world. This is contact page.")
    return render(request,'contact.html')
