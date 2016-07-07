from django.shortcuts import render
from django.core.paginator import Paginator

import requests
from bs4 import BeautifulSoup


# Create your views here.


def guitar_scraping_view(request):
    song = request.GET.get('song') or "yesterday once more"
    url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(song)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    songs = str(souper.find(class_="tabslist"))

    return render(request,"index.html",{"songs":songs})


def tablature_scrape_view(request):
    song_tab = request.GET.get('song')
    url = "http://www.guitartabs.cc/tabs/{}/{}/{}".format('letter', 'band', 'song')
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    song_tabs = str(souper.find(class_="tabscont"))

    return render(request, "detail.html", {"song_tabs":song_tabs})
