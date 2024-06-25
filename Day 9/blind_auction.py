import assets as asset
import os
print(asset.logo)

bid = {}

should_continue = True

while should_continue:
    new_name = input("What is your name? :")
    new_bid = int(input("What is your bid? :$"))
    bid[new_name] = new_bid
    can_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    should_continue = can_continue.lower() == "yes"
    os.system('cls')

highest_bider = ""
for bider in bid:
    if highest_bider == "":
        highest_bider = bider
    elif bid[bider] > bid[highest_bider]:
        highest_bider = bider
print(f"The winner is {highest_bider} with a bid of ${bid[highest_bider]}")