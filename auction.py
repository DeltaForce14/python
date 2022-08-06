



#empty dictionary to add names and bids to
bids = {}

# variable that ends the while loop
next_bid = True

# Adding info into diftionary
while next_bid:
    # Questions
    name_bidder = input("What is your name?\n")
    bid_bidder = input("what is your bid?\n")
    # adding info from Questions into dictionary
    bids.update({name_bidder: bid_bidder,})
    bidder_next = input("Are you the last bidder? 'Yes or 'No' \n").lower()

    # turning next_bid variable to False to stop the while loop 
    if bidder_next == "yes":
        next_bid = False

# Finding winner
def winner(bid_dict):
    # Who is the top bidder? Emtpy list where values are appended
    bids_value= []

    # looping through key and appending values into list as integers
    for key in bids:
        bids_value.append(int(bids[key]))

    # finding highets integer among bids and changing to string to be able to compare it
    #to the value in a dictonary which is string 
    winning_bid = str(max(bids_value))

    # getting key of the highest value. Looping through both keys and values in bids dictionary
    # comparing value to the highest bid and getting its key
    for key, value in bids.items():
        if value == winning_bid:
            print(f"The highest bidder is {key} with ${winning_bid}.")

winner(bids)            


