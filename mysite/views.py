from django.shortcuts import render
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect

def deconnexion(request):
    logout(request)
    return redirect('/client/Home')
def accueil(request):
    return render(request,'accueil.html' )