# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_sm = 2
pepperoni_md_lg = 3
more_cheese = 1

bills = 0
if size == 'S':
    bills += small_pizza
elif size == 'M':
    bills += medium_pizza
else:
    bills += large_pizza

if add_pepperoni == 'Y':
    if size == 'S':
        bills += pepperoni_sm
    else:
        bills += pepperoni_md_lg

if extra_cheese == 'Y':
    bills += more_cheese

print(f"Your final bill is: ${bills}")
