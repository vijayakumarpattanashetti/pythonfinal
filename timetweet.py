import os
import time
import tweepy
consumer_key='LYtkfKiEhvZC8ESwKhjrWzW0x V'
consumer_secret='yYA6rSrviGciwjpzJWlIqYg0PG6opeIL9CbaNOSUzxgclA2MVW V'
access_token='899683933712859136-1j7j7JBvthNB0PxhTUVvLsPv84bqgnE V'
access_token_secret='OBej4V3amu0OG0yS0M66dvpO9aKz6SzJueS8O4C2J1v7P V'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

a=1
while (a<4):
    os.system("fswebcam -F 5 --fps 20 -r 1200*800 /home/pi/vvv/w.jpg")
    i="/home/pi/vvv/w.jpg"
    print("pic taken")
    api.update_with_media(i,status="jUsT aMaZiNg")
    print('DONE')
    time.sleep(15)
    print("DONE")
    a+=1
