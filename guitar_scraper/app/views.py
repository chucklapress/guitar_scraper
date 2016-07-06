from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def guitar_scraping_view(request):
    song = request.GET.get('song') or "NIB"
    artists = request.GET.get("song")
    url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(song)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    songs = souper.find_all(class_="ryzh22")

    link = [link["href"] for link in souper.find_all(class_="ryzh22")]




    return render(request,"index.html",{"link":link})
