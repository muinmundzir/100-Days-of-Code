# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_count = input("How many people to split the bill? ")

bill_in_float = float(bill)
tip_in_int = int(tip)
people_count_in_int = int(people_count)

payment_amount = (bill_in_float / people_count_in_int) * \
    (1 + (tip_in_int / 100))
result = f"Each person should pay: ${round(payment_amount, 2)}"

print(result)
