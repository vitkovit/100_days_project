from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.


print(logo)

biders_dictionary = {}
other_user = "no"
while other_user == "no":
    bidder_name = input("bidder name: ")
    bid_price = int(input("bid price: "))

    biders_dictionary[bidder_name] = bid_price
    other_user = input("Last user? (yes or no): ")
    if other_user == "no":
        clear()
#     print(biders_dictionary)

bid_winner_price = max(biders_dictionary.values())

bid_winner_name = ""
for key in biders_dictionary:
    if biders_dictionary[key] == bid_winner_price:
        bid_winner_name = key


 # type: ignore
print(f"the winner is {bid_winner_name} with bid: {bid_winner_price} gold")
print("here are resutls")
print(biders_dictionary)

""" solution from course
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

"""