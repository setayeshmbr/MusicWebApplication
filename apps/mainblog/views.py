from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'mainblog/index.html')

def profile(request):
    return render(request,'mainblog/profile.html')