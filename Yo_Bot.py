#I heard you like to Yo, so Yo_Bot spams your friends with Yo
#Robert Piston

import requests
from time import sleep

num_spams = 10      #how many times you want to spam Yo
api_token = '<your API token here>'  #your personal Yo API token.  Get a token at http://yoapi.justyo.co/

friends = ('Friend1', 'Friend2', 'Friend3', 'etc')  #a list of your friends' Yo usernames

def yo_bot(api_token, username):   #function to Yo a specific username
    return requests.post("http://api.justyo.co/yo/", data={'api_token': api_token, 'username': username})

def yo_all(api_token):             #function to Yo all subscribers.  Note: a person must Yo you first to become a subscriber
    return requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})

#loop to Yo specific users defined in your list
for count in range(num_spams):     
    sleep(60)                      #Yo API permits one Yo per minute
    for value in friends:          #loop sends a Yo to each of the usernames in your friends list
        yo_bot(api_token, value)
    print "A 'Yo' has been sent to: %s" %(", ".join(friends))
    
# #loop to Yo your subscribers for a specified number of times
# for count in range(num_spams)
#     sleep(60)
#     yo_all(api_token)