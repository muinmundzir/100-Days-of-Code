# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
merge_name = name1 + name2
t = merge_name.lower().count("t")
r = merge_name.lower().count("r")
u = merge_name.lower().count("u")
e = merge_name.lower().count("e")
true = t + r + u + e

l = merge_name.lower().count("l")
o = merge_name.lower().count("o")
v = merge_name.lower().count("v")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score > 90 or love_score < 10:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score <= 50 and love_score >= 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
