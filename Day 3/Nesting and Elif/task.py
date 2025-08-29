print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    age = int(input("What is your age? "))
    if age > 18:
        print("Ticket price $12!")
    elif age > 12:
        print("You get a goooooood deeeeeal! $7")
    else:
        print("WOW, ticekt price $5")
else:
    print("Sorry you have to grow taller before you can ride.")
