from get_image import get_image as gi
from imager import imager
from tw import tw

file = open('persian_list', 'rt')

list = file.read().split()
parent_id = None

for word in list:
	r = gi.get_image(word)
	img = imager.create_img(r, word)
	byte = img.tobytes()
	parent_id = tw.post_meme(img, parent_id)
	img.save("outputs/" + word + ".png")
