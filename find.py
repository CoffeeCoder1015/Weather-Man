import requests
from bs4 import BeautifulSoup
import re

header = {
    'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'none',
    'Accept-Language':'en-US;q=0.8',
    'Connection':'keep-alive'
}

def current():
    Req = requests.get("https://weather.com/en-NZ/weather/today/",headers=header)
    print(Req.url)
    Page = Req.text
    Page_FMT = BeautifulSoup(Page,features='html.parser').prettify()
    Page_FMT = "".join([len(re.findall(r"^(\s)",i))*3*" "+i+"\n" for i in Page_FMT.split("\n")])