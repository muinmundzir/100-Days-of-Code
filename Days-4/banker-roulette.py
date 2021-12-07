import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names_list = names_string.split(', ')
index = random.randint(0, len(names_list) - 1)
person_who_pay = names_list[index]

print(f"{person_who_pay} is going to buy the meal today!")
