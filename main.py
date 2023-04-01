from art import logo
import random
import os

def listing_bidders(bidders):
    bid_list = []
    bid_dict = {}
    for _ in range(bidders):
        clear()
        name = input("What is your name? - ")
        bid = int(input("What is your bid? - "))
        bid_dict = {name: bid}
        bid_list.append(bid_dict)
    
    return bid_list

def filter_bid(bid_list):
    for bidders in bid_list:
        for key in bidders:
            if bidders.get(key) < winning_bid:
                bid_list.remove(bidders)

def find_minimum(bid_list):
    for key in bid_list[0]:
        minimum_bid = bid_list[0][key]
        minimum_name = key
        
    for bidders in bid_list:
        for key in bidders:
            if bidders[key] < minimum_bid:
                minimum_bid = bidders[key]
                minimum_name = key
                
    return minimum_name, minimum_bid

clear = lambda: os.system('cls')

print(logo)

print("Welcome To The Undercover Auction. Please Read The Rules Below.\n")

print("1. A random winning bid amount is generated and kept a secret.\n 2. Players will take turns bidding on the winning bid amount, without knowing what the winning bid amount is\n 3. Players will bid in whole numbers only\n 4. The player with the LOWEST BID that is equal to or greater than the winning bid amount will win the auction.\n 5. If there are no bids that are equal to or greater than the winning bid amount, the auction will be canceled.\n 6. The game ends when a player wins the auction.\n 7. The winner will be announced at the end of the game, along with the winning bid amount.\n")

winning_bid = round(random.random() * 100)

# print(winning_bid)

number_of_bidders = int(input("How Many Bidders Will Join? - "))

list_of_bidders = listing_bidders(number_of_bidders)

# Filtering bids which is less than the winning bid
filter_bid(list_of_bidders)

# Find the minimum bidder
minimum_name, minimum_bid = find_minimum(list_of_bidders)

print("Congratulation!!")
print(f"{minimum_name} won with the minimum bid and the bid was {minimum_bid}")