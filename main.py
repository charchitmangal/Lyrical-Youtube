from bs4 import BeautifulSoup
import requests


def get_lyrics(youtube_title):

    # requesting page
    page = requests.get("https://genius.com/search?q=" + youtube_title)

    # parsing 
    soup = BeautifulSoup(page.content, 'html.parser')

    #get link for lyrics page
    lyrics = soup.find_all("a", {"class" : "mini_card"})

    print(lyrics)



get_lyrics("Coldplay - Hymn For The Weekend (Official Video)")



