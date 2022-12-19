# Use dictionaries and lists to create a silent auction program

import os
import time

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
Welcome to the Silent Auction! Please state your name and make your bid!
'''
moreEntries = True
bids = {}

while moreEntries:
    print(logo)
    time.sleep(2.5)
    os.system('clear')
    name = input("Please enter your name: \n")
    bid = input(f"Please enter your bid {name}: $ ")
    # add name and bid to bids dictionary
    bids[name] = bid
    keepGoing = input(f"{name}, are there others that wish to bid? Please type 'yes' or 'no': ")
    # decide if there are more bidders
    if keepGoing == 'no':
        moreEntries = False

# select winner
winner = max(bids.keys())
print(f"The bids were {bids}")
print(f"The winner of this auction is {winner}")
print(type(bids["sid"]))