from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Tempat, Resep
import requests

# Create your views here.
def sinkron_resep(request):
    URL = "https://masak-apa-tomorisakura.vercel.app/api/recipes/1"
    
    r = requests.get(url = URL)        
    data = r.json()        
    
    for d in data["results"]:
        print(d['key'])
        cek_resep = Resep.objects.filter(key=d['key'])
        if cek_resep.exists():
            resep = cek_resep.first()
            resep.title = d['title']
            resep.thumb = d['thumb']
            resep.key = d['key']
            resep.times = d['times']         
            resep.save()
        else:
            Resep.objects.create(
                title = d['title'],
                thumb = d['thumb'],
                key = d['key'],
                times = d['times'],
            )
    ambil_resep = Resep.objects.all()
   
    for ambil in ambil_resep:
        url_detil_resep = "https://masak-apa-tomorisakura.vercel.app/api/recipe/{}".format(ambil.key)
        print(url_detil_resep)
        r = requests.get(url_detil_resep,ambil.key)     
        data = r.json()['results']        
        ambil.step = data['step']
        ambil.ingredient = data['ingredient']
        ambil.save()
    return HttpResponse("<h1>berhasil sinkron</h1>")  

@login_required
def resep(request):
    template_name = "backend/resep/resep.html"
    resep_list = Resep.objects.all()
    context = {
        'title' : 'Data Resep',
        'resep' : resep_list,
    }
    return render(request, template_name, context)

@login_required
# Membuat view detail resep
def resep_detail(request, key):
    #mengambil data resep berdasarkan key
    ambil_resep = Resep.objects.all()
   
    for ambil in ambil_resep:
        url_detil_resep = "https://masak-apa-tomorisakura.vercel.app/api/recipe/{}".format(ambil.key)
        print(url_detil_resep)
        r = requests.get(url_detil_resep,ambil.key)     
        data = r.json()['results']        
        ambil.step = data['step']
        ambil.ingredient = data['ingredient']
        ambil.save()
    return HttpResponse("<h1>berhasil sinkron</h1>")
    template_name = "backend/resep/detail.html"
    context = {
        'title' : "Halaman Detail Resep"
    }
    return render(request, template_name, context)

@login_required
def resep_detil(request, key):
    template_name = "backend/resep/resep_detail.html"
    resep = Resep.objects.get(key=key)
    dresep = Resep.objects.all()
    ingredient = resep.ingredient.replace("[", "").replace("]", "").replace("', '", "-").replace("'","").replace("-", "\n")
    step = resep.step.replace("[", "").replace("]", "").replace("', '", "-").replace("'","").replace("-", "\n")
    context = {
        'title' : 'Detail Data Resep',
        'resep' : resep,
        'dresep': dresep,
        'step' : step,
        'ingredient' : ingredient,
    }
    return render(request, template_name, context)


@login_required
def dashboard(request):
    template_name = "backend/dashboard.html"
    context = {
        'title' : 'dashboard',
    }
    return render(request, template_name, context)

@login_required
def tempat(request):
    template_name = "backend/lokasi/lokasi.html"
    tempat_list = Tempat.objects.all()
    context = {
        'title' : 'Data Lokasi Restoran Terdekat',
        'tempat' : tempat_list,
    }
    return render(request, template_name, context)

@login_required
def tambah_lokasi(request):
    template_name   = "backend/lokasi/tambah.html"
    if request.method == "POST":
        input_nama = request.POST.get('nama')
        input_thumb = request.POST.get('thumb')
        input_alamat = request.POST.get('alamat')
        input_kontak = request.POST.get('kontak')
        
        #simpan lokasi
        Tempat.objects.create(
            nama = input_nama,
            thumb = input_thumb,
            alamat = input_alamat,
            kontak = input_kontak,
        )
        return redirect(tempat)
    context = {
        'title' : "Form Tambah Data Lokasi"
    }
    return render(request, template_name, context)

# edit lokasi
def ubah_lokasi(request, id):
    template_name = "backend/lokasi/tambah.html"
    get_lokasi = Tempat.objects.get(id=id)
    if request.method == "POST" :
        input_nama = request.POST.get('nama')
        input_thumb = request.POST.get('thumb')
        input_alamat = request.POST.get('alamat')
        input_kontak = request.POST.get('kontak')
        
        # menyimpan 
        get_lokasi.nama = input_nama
        get_lokasi.thumb = input_thumb
        get_lokasi.alamat = input_alamat
        get_lokasi.kontak = input_kontak
        get_lokasi.save()
        return redirect(tempat)
    context = {
        'title' : 'Form Ubah Data Lokasi',
        'get_lokasi': get_lokasi,
    }
    return render(request, template_name, context)

# menghapus 
def hapus_lokasi(request, id):
    Tempat.objects.get(id=id).delete()
    return redirect(tempat)