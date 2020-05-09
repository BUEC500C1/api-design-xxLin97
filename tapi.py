import tweepy
from google.cloud import vision

def load_image(consumer_key, consumer_secret, key, secret, access_token, access_token_secret, userid):
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    API = tweepy.API(auth)

    user = API.get_user(userid)
    tweets = api.user_timeline(id=userid)

    
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
key = ""
secret = ""
userid = ""
    
    for status in tweepy.Cursor(api.user_timeline, id="userid").items():
        if 'media' in status.entities:
            for images in status.entities['media']:
                image.source.image_uri = images['media_url']
                response = client.label_detection(image=image)
                print(f"image at {images['media_url']} contains:")
                for label in response.label_annotations:
                    print(label.description)


load (consumer_key, consumer_secret, key, secret,access_token,access_token_secret,user_id)