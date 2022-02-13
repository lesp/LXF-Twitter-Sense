#!/usr/bin/env python3
import tweepy
from sense_hat import SenseHat
from datetime import datetime
sense = SenseHat()
client = tweepy.Client(consumer_key='YOUR API KEY',
                       consumer_secret='YOUR API KEY SECRET',
                       access_token='YOUR ACCESS TOKEN',
                       access_token_secret='YOUR ACCESS TOKEN SECRET')

temp = round(sense.get_temperature(),1)
now = datetime.now()
current_time = now.strftime("%H:%M")
funny = ["Right now the temperature at my desk is ", "Oh my word it is cold at my desk, it is only ", "Feeling hot, hot, hot, the temperature is "]
if temp < 22.0:
    msg = current_time+" "+[1]+str(temp)+" Celsius"
elif temp > 23.0:
    msg = current_time+" "+funny[2]+str(temp)+" Celsius"
else:
    msg = current_time+" "+funny[0]+str(temp)+" Celsius"

response = client.create_tweet(text=msg)
print(response)
print(msg)
sense.show_message(str(temp)+"C")
