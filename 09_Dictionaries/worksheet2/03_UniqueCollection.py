'''The Unique Collector’s Auction
You’re at a collector’s auction. Each lot number is a key, and the value is the type of collectible. 
Auctioneers want to quickly know how many unique collectibles are being auctioned, not just the number of lots. 
Can you wow them with an instant count?
Input: auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
Expected Output: Unique collectibles: ['coin', 'stamp', 'comic']'''


import ast
auction=input("Enter the auction details:")
auction=ast.literal_eval(auction)

l=[]
for key,value in auction.items():
    if value not in l:
        l.append(value)
print("unique collectibles:",l)
