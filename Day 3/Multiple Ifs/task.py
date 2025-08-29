print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

price = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        price = 5
        #print("Please pay $5.")
    elif age <= 18:
        price = 7
        #print("Please pay $7.")
    else:
        price = 12
        #print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


photo = input("Do you want a photo (Y/N) ")
if photo == "Y":
    price += 3

print(f"Your ticked costs ${price}")
