from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def guitar_scraping_view(request):
    artists = request.GET.get("artists")
    url = "http://www.guitartabs.cc/search.php?tabtype=any&band={}".format(artists)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    

    return render(request,"index.html",{"artists":artists,"bands":bands})
