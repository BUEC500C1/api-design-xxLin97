import json

import api

from google.cloud import vision



def anaylze(tweets):

  image_uri = tweets

  for i in image_uri:

    client = vision.ImageAnnotatorClient()

    image_to_open = vision.types.Image()

    image_file_uri = i



   image = vision.types.Image(content=content)text_response = client.text_detection(image=image)



    
if __name__ == '__main__':

  getpicture.get_tweets(input('input id'))

  tweets = []

  with open('tweet.json') as f:

    tweets = json.load(f)

  anaylze(tweets)