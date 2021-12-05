print("Welcome to the rollercoaster!")
height = int(input("Enter your height: "))

pay = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age > 18:
        pay += 12
        print(f'Child ticket are: ${pay}')
    elif age < 12:
        pay += 5
        print(f'Youth ticket are: ${pay}')
    elif age > 44 and age < 56:
        print(f'Everything is going to be ok. Have a free ride on us')
    else:
        pay += 7
        print(f'Adult ticket are: ${pay}')
    take_photo = input("Want to take photos? Y or N")
    if take_photo == 'Y':
        pay += 3
    print(f"Please pay ${pay}")
else:
    print("You can't ride")
