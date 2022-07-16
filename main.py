from get_image import get_image as gi
from imager import imager
from tw import tw
import sys
import argparse
import os

# Arguments parser config
parser = argparse.ArgumentParser()
parser.add_argument("--language", default="fa", help="language (fa/en)", type=str)
parser.add_argument("--twitter", default=False, help="Should post on twitter")
args = parser.parse_args()

# Replace old data
os.system("rm -rf outputs && mkdir outputs")


file = open('persian_list', 'rt')
if (args.language == 'en'):
	file = open('english_list', 'rt')

list = file.read().split()
parent_id = None

for word in list:
	r = gi.get_image(word)
	img = imager.create_img(r, word)
	byte = img.tobytes()
	if (args.twitter):
		parent_id = tw.post_meme(img, parent_id)
	img.save("outputs/" + word + ".png")
