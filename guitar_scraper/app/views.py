from django.shortcuts import render
from django.core.paginator import Paginator

import requests
from bs4 import BeautifulSoup


# Create your views here.


def guitar_scraping_view(request):
    song = request.GET.get('song') or "NIB"
    url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(song)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    songs = str(souper.find(class_="tabslist"))








    return render(request,"index.html",{"songs":songs})
