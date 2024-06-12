print("This is just a day 2 project to share bill with others")
bill = float(input("What is the amount need to pay: $"))
tip_in_persentage = float(input("how much persentage do you want to give tip need to be greater than 0: "))
no_of_people_to_share = int(input("Number of people you need to share bill with: "))
tip = bill * tip_in_persentage / 100
total_amount = bill + tip
share_amount = round(total_amount / no_of_people_to_share , 2)
print(f"Each person should share ${share_amount} in the bill")
