from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import PJ

# Create your views here.

def index(request):
        list_pj = PJ.objects.all()
        context = {"listpj" : list_pj}
        return render(request, 'pages/home.html', context)

'''
def index(request):
        duong_dan = "https://drive.google.com/drive/folders/1kfK7D3su0zYPuXWldbEVSs_JMWiSln2w?usp=sharing"
        ten_pj = "Keo bua bao"
        id_pj = 1
        context = {"duongdan" : duong_dan, "tenpj" : ten_pj, "stt" : str(id_pj)}
        return render(request, 'pages/home.html', context)
'''