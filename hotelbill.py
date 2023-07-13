# HOTEL BILL

ratePerDay = 1500
airconFee = 500
internetFee = 300
tvFee = 100
evat = .12


numberOfDays = int(input("Enter Number of Days: "))

# formula for the amount
amount = ratePerDay * numberOfDays

# formula for the total amount
totalAmount = amount + airconFee +internetFee + tvFee


# formula for the tax
tax = totalAmount * evat


# formula for the bill
bill = totalAmount + tax

print("The total bill is: ", bill)
