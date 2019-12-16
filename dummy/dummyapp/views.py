from django.shortcuts import render, redirect
from django.http import HttpResponse
from dummyapp.forms import Imageform
# Create your views here.

def index(request):
    return render(request,'dummyapp/index.html',)
def other(request):
    return render(request,'dummyapp/other.html')
def relative(request):
    return render(request,'dummyapp/relative_url.html')

def image(request):
    if request.method=='POST':
        form=Imageform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return render(request,'dummyapp/success.html')
    else:
        form=Imageform()
        return render(request,'dummyapp/upload.html',{'form':form})

def gallery(request):
    return render(request,'dummyapp/gallery.html')