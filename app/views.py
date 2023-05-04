from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
# Create your views here.
from django.http import HttpResponse

def Register(request):
    UFO=Userform()
    PFO=Profileform()
    d={'UFO':UFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:
        UFD=Userform(request.POST)
        PFD=Profileform(request.POST,request.FILES)

        if UFD.is_valid() and PFD.is_valid():

            NSUO=UFD.save(commit=False)
            NSUO.set_password(UFD.cleaned_data['password'])
            NSUO.save()


            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()


            send_mail('Register',
                       'successfully Register is done ',
                       'Ganeshgs63019@gamil.com',
                       [NSUO.email],
                       fail_silently=False
                       )
            return HttpResponse('registation is successfully...........')
    

        else:
            return HttpResponse('data is not valid')

    return render(request,'Register.html',d)