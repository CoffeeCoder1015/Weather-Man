import requests
from bs4 import BeautifulSoup
header = {
    'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'none',
    'Accept-Language':'en-US;q=0.8',
    'Connection':'keep-alive'
}

def current():
    requests.get("https://weather.com/weather/todays").content
