
another_person = True
auction = {}

# Collecting bids
while another_person:
    name = input("Name: ")
    bid = int(input("Bid: "))

    auction[name] = bid
    add_people = input("Add another person? Yes or no: ").lower()
    if add_people == "no":
        another_person = False

# Print all bids
print("Auction results:", auction)

# Find the highest bid
highest_bid = 0
highest_bidder = ""

for person in auction:
    if auction[person] > highest_bid:
        highest_bid = auction[person]
        highest_bidder = person

# Print the highest bid and the winner
print(f"Highest bid is by {highest_bidder} with a bid of {highest_bid}.")
