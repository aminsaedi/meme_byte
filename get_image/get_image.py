import requests
from bs4 import BeautifulSoup
import sys

def get_image(word):
	url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X" % word
	text = requests.get(url).text
	soup = BeautifulSoup(text, 'html.parser')

	try:
		return (soup.find_all("img")[1]['src'])
	except:
		return (None)
