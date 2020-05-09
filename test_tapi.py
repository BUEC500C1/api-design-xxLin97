 
import pytest
import tapi 

def if_get_tweets_right():
  tweets = []
  with open('tweet.json') as file:
    tweets = json.load(file)
  image_uri = tweets
  for i in tweets:
    if i.endswith(".jpg"):
      continue
    else:
      print('pass error')
      return
  print("tweet pass")

  #test if get images from twitter
def if_tapi_pass():
  Tw = tapi.get_all_tweets("Tweets")
  if len(Tw) == 0:
    print("pass error")
    return
  print("pass test")


def if_gvision_pass():

  name = input("get tweet name")
  pyy.get_all_tweets(name)
  googlevision.getdescription()

if __name__ == '__main__':
  if_get_tweets_right()
  if_tapi_pass()
  if_gvision_pass()
  
test_result()