import requests
import bs4

index = 'http://tidesandcurrents.noaa.gov/tide_predictions.html'
response = requests.get(index)

soup = bs4.BeautifulSoup(response.text)

f = open('soup1.txt','w')
f.write(repr(soup))
f.close


