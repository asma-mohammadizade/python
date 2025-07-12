# the secret auction program

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo
print(logo)

namebid = {}
bidding_finished = False

def highest_bidder(bidding_data):
    heighest_bid = 0
    winner = ""
    for bidder in bidding_data:
        bid_amount = bidding_data[bidder]
        if bid_amount > heighest_bid:
            heighest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${heighest_bid}.")

while not bidding_finished:
    print("Welcome to the secret auction program")
    name = input("what is your name? ")
    cost = int(input("what's your bid? $"))
    namebid[name] = cost
    other_bidders = input("are there any other bidders? type 'yes' or 'no': ")  
    if other_bidders == "no":
        bidding_finished = True
        highest_bidder(namebid)
    elif other_bidders == "yes":
        clear()
        