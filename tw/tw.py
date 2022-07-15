from twitter import *
from io import BytesIO
import os

token=os.environ['TOKEN']
token_secret=os.environ['TOKEN_SECRET']
consumer_key=os.environ['CONSUMER']
consumer_secret=os.environ['CONSUMER_SECRET']


t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))



def post_meme(image, parent_id):
	output = BytesIO()
	image.save(output, format='PNG')
	t_upload = Twitter(domain='upload.twitter.com',auth=OAuth(token, token_secret, consumer_key, consumer_secret))
	id = t_upload.media.upload(media=output.getvalue())["media_id_string"]
	result = t.statuses.update(status="PTT ★", media_ids=",".join([id]), in_reply_to_status_id=parent_id)
	return result['id']
