#! /Users/amin/.local/share/virtualenvs/meme_byte-DudDzkl7/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

word = sys.argv[1]
url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X" % word
text = requests.get(url).text
soup = BeautifulSoup(text, 'html.parser')

try:
	print (soup.find_all("img")[2]['src'])
except:
	print (None)
