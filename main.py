import requests
from bs4 import BeautifulSoup


def guitar_scraping_view():

    url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song=yesterday"
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    songs = souper.find_all(class_="ryzh22")
    for song in songs:
        print(song.attrs["href"])



guitar_scraping_view()
