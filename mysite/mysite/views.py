from django.shortcuts import render, redirect #untuk memanggil halaman  html
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse #format html langsung ditulis didalam httpresponse
from resep.models import Resep
import requests


# Home
def index(request):
    template_name = 'front/index.html'
    context = {
        'title'     : 'Halaman Awal',
    }
    return render(request, template_name, context)

def resep(request):
    template_name = 'front/resep.html'
    resep = Resep.objects.all()        
    context = {
        'title' : 'Resep',
        'resep' : resep
    }
    return render(request, template_name, context)

def resep_detil(request, key):
    template_name = 'front/resep_detil.html'
    resep = Resep.objects.get(key=key) 
    context = {
        'title' : 'Resep',
        'resep' : resep
    }
    return render(request, template_name, context)


def tempatmakan(request):
    template_name = 'front/tempatmakan.html'
    context = {
        'title' : 'Rekomendasi Tempat Makan',
    }
    return render(request, template_name, context)

def kontak(request):
    template_name = 'front/kontak.html'
    context = {
        'title' : 'Kontak Kami',
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        print('sudah login')
        return redirect('index')
    
    template_name = 'account/form-login.html'
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            #data ada   
            print('Username Benar')
            auth_login(request, user)
            return redirect('index')
        else :
            #data tidak ada
            print('Akun tidak ditemukan')
        
    context ={
        'title' : 'Form Login',
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('index')
    