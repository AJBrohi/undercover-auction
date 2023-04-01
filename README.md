# Undercover Auction

This program is a Python implementation of an undercover auction where bidders submit their bids without knowing the bid of other bidders. The program finds the minimum bid greater than or equal to the winning bid and declares the winner.

## Rules

1. The auction is for a single item.
2. All bidders must submit their bid without knowing the bid of other bidders.
3. The bid must be greater than or equal to the minimum bid to be considered.
4. The minimum bid is calculated as the minimum bid greater than or equal to the winning bid.
5. The winner is the bidder with the MINIMUM BID greater than or equal to the winning bid.

## Program Features

This program includes the following features:

- User input for the number of bidders participating in the auction
- User input for each bidder's name and bid amount
- Filtering of bids that are less than the randomly generated winning bid
- Identification of the winning bidder with the highest bid above the randomly generated winning bid

## Python Features
This program utilizes the following Python features:

- random module for generating a random winning bid
- User-defined functions for creating a list of bidders, filtering bids, and finding the winning bidder
- Use of dictionaries to store bidder names and bid amounts
- Use of loops to iterate over the list of bidders and bids
- Use of conditional statements to filter bids and determine the winning bidder

## How to use

- Clone the repository to your local machine.
- Open the terminal and navigate to the directory where the repository is cloned.
- Run the command python `main.py` to start the program.
- Follow the instructions to input the number of bidders and their bids.
- The program will output the name and the bid of the winner.

## Test Run
![9_undercover_auction](https://user-images.githubusercontent.com/29802859/229309788-4b29867a-18f3-4bb0-a374-6af25bb86547.gif)
