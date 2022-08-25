# 1.ornek

# import random
#
# bill = input("Bill: ")
#
# bill = bill.replace("$","")
#
# bill = float(bill)
#
# percents = ["15", "18", "20"]
#
# random_percent = int(random.choice(percents))
#
# tip = bill * random_percent / 100
#
# print(f"Suggested tip: ${tip:.2f}")

#inputs and variables



#2.ornek

bill = float(input("How much did your meal cost? "))

tip = int(input("how much tip do you want to add 15% , 18% or 20% ?? "))

tax = 0.05

#math calculations

tax_amt = bill * tax

tip_amt = bill * tip/100

total = bill + tip_amt + tax_amt

#printing

print(f"Your Bill is ${bill:.2f} and your tip is ${tip_amt:.2f} ")

print(f"Your total with tax is ${total:.2f}")




