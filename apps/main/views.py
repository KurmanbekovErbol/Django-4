from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset, 'index.html', locals())
    
def about(requset):
    return render(requset, 'about.html', locals())