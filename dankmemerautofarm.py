import requests
import colorama
from colorama import Fore
import time
from time import sleep
import os

counter = 0

file = open("token.txt")
data = file.read()

def autofarm(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    
    r = requests.post(url, data=data, headers=header)

    if r.status_code == 429:
        print("Rate limited please wait!")
    elif r.status_code == 200:
        print("Sent!")

message1 = 'pls beg'
message2 = 'pls fish'
message3 = 'pls hunt'
message4 = 'pls dig'

os.system('title dank memer auto farm by Harvey')

start = input(Fore.MAGENTA + """
                                              made by: ! Harvey#2702

             █████╗ ██╗   ██╗████████╗ ██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
            ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
            ███████║██║   ██║   ██║   ██║   ██║█████╗  ███████║██████╔╝██╔████╔██║█████╗  ██████╔╝
            ██╔══██║██║   ██║   ██║   ██║   ██║██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║██╔══╝  ██╔══██╗
            ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
            ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                      
                                                1: start
                                                2: betting

                                                     """)

if start == '1':
    channelid = input("Channel id: ")
    patreon = input("Are you a patreon member? y/n ")
    autofarm(data, channelid, 'pls daily')
    autofarm(data, channelid, 'pls weekly')
    autofarm(data, channelid, 'pls monthly')
    while 3 == 3:
        autofarm(data, channelid, message1)
        autofarm(data, channelid, message2)
        autofarm(data, channelid, message3)
        autofarm(data, channelid, message4)
        counter = counter + 1
        if counter >= 25:
          autofarm(token, channelid, 'pls dep all')
          counter = counter - 25
        if patreon == 'y':
          time.sleep(25.15)
        elif patreon == 'n':
          time.sleep(35.15)
        else:
          print("Invalid statement!")
          quit()
          
elif start == '2':
    patreon = input("Are you a patreon member? y/n ")
    channelid = input("Channel id: ")
    betam = int(input("Bet amount: "))
    while betam >= 250001 or betam <= 1499:
      if betam >= 250001:
        print("Bets can not be over 250001")
        betam = int(input("Bet amount: "))
      elif betam <= 1499:
        print("Bets can not be less than 1500")
        betam = int(input("Bet amount: "))
    while 3 == 3:
        autofarm(data, channelid, 'pls bet ' + str(betam))
        print("Sent!")
        if patreon == 'y':
          time.sleep(3)
        elif patreon == 'n':
          time.sleep(5)
        else:
          print("Invalid statement!")

else:
    print("Invalid statement!")
