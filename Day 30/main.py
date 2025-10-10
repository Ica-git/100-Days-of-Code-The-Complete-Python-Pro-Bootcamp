
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     contents = file.read()
#     print(contents)
# finally:
#     raise TypeError("GRESKA!")

height = float(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

if height > 300:
    raise TypeError("Human height shouldn't be over 3 meters")

bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

