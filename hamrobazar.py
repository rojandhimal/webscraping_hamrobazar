import requests
from bs4 import BeautifulSoup

URL = 'https://hamrobazaar.com/c112-real-estate'


def getData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    return soup

x = getData(URL)
text = x.find("td", { "id" : "tab_cat1" })
print(text)



