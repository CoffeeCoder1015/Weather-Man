import requests
from bs4 import BeautifulSoup
import re
from geopy import Nominatim

geolocator = Nominatim(user_agent="gsll")

header = {
    'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'none',
    'Accept-Language':'en-US;q=0.8',
    'Connection':'keep-alive'
}

def currentWeather():
    Req = requests.get("https://weather.com/en-NZ/weather/today/",headers=header)
    print(Req.url)
    Page = Req.text
    Page_FMT = BeautifulSoup(Page,features='html.parser')
    weather_dat = Page_FMT.find("div",{"id":"WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"})
    tlsblk = weather_dat.find("div",{"class":"CurrentConditions--header--3-4zi"})
    location = tlsblk.find("h1",{"class":"CurrentConditions--location--1Ayv3"}).text
    time = tlsblk.find("div",{"class":"CurrentConditions--timestamp--1SWy5"}).text
    tls = f"{location} {time}"
    cur1 = weather_dat.find("div",{"class":"CurrentConditions--primary--3xWnK"})
    cur2 = weather_dat.find("div",{"class":"CurrentConditions--secondary--2XNLR"})
    return [tls,cur1.text,cur2.text]

def gsll(location):
    location = geolocator.geocode(str(location))
    print(location.latitude,location.longitude)