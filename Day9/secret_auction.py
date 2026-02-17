import asci_art
import os

print('Welcome to the Blind Auction')
print(asci_art.LOGO)

bids = {}
max_bid = 0
max_bid_by = ''
while True:
  name = input('Enter your Name:')
  bid = int(input('Enter your Bid:'))
  if bid > max_bid:
    max_bid = bid
    max_bid_by = name
  bids[name] = bid
  to_continue = input('Is there any one else(Y/N):')
  
  if to_continue == 'N':
    break
  else:
    os.system('clear')

print('Bids are As follows:')

for name, bid in bids.items():
  print(f"{name} with a bid of ${bid}")

print(f"Winner of this auction is {max_bid_by} with a bid of ${max_bid}")