import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is : {winner}, with a bid of ${highest_bid}!")
more_bidders = True
bid = {}
while more_bidders:
    name = str(input("What is your name?"))
    price = int(input("How much do you want to bid? $"))
    more = input("Are there more bidders? yes or no: " )
    print("\n" * 50)
    bid[name] = price
    if more == "no":
        more_bidders = False
        find_highest_bidder(bid)



