from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import re
import arabic_reshaper
from bidi.algorithm import get_display

def get_octa_img(img, word):
	font = ImageFont.truetype("Vazirmatn-Medium.ttf", 30)
	img_size = img.resize((100,100))
	octa_img = Image.new("RGB", (400, 250), "white")
	draw = ImageDraw.Draw(octa_img)
	word = re.sub(r"بیت$", "بایت", word)
	word = arabic_reshaper.reshape(word)    # correct its shape
	word = get_display(word) 
	draw.text((0, 0), word, (0, 0, 0), font=font)
	octa_img.paste(img_size, (0, 50))
	octa_img.paste(img_size, (100, 50))
	octa_img.paste(img_size, (200, 50))
	octa_img.paste(img_size, (300, 50))
	octa_img.paste(img_size, (0, 150))
	octa_img.paste(img_size, (100, 150))
	octa_img.paste(img_size, (200, 150))
	octa_img.paste(img_size, (300, 150))
	return octa_img

def get_single_img(img, word):
	font = ImageFont.truetype("Vazirmatn-Medium.ttf", 30)
	img_size = img.resize((100,100))
	img = Image.new("RGB", (400, 150), "white")
	draw = ImageDraw.Draw(img)
	word = arabic_reshaper.reshape(word)    # correct its shape
	word = get_display(word)
	draw.text((0, 0), word, (0, 0, 0), font=font)
	img.paste(img_size, (0, 50))
	return img

def merge(single_img, octa_img):
	img = Image.new("RGB", (400, 400), "white")
	img.paste(single_img, (0, 0))
	img.paste(octa_img, (0, 150))
	return img

def create_img(url, word):
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	single = get_single_img(img, word)
	octa = get_octa_img(img, word)
	result = merge(single, octa)
	return result
		
