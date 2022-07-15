from get_image import get_image as gi
import os
from imager import imager

output_stream = os.popen("cat /usr/share/dict/words | egrep bit$")
list = output_stream.read().split()

for word in list:
	r = gi.get_image(word)
	img = imager.create_img(r, word)
	img.save("outputs/" + word + ".png")
