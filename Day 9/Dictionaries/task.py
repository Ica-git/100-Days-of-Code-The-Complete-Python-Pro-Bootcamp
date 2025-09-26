# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
#
# print(programming_dictionary["Bug"])
#
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
#
# programming_dictionary["Bug"] = "A moth in your computer."
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["Paris", "Nice", "Grenoble"],
#     "Germany": ["Berlin", "Stuttgart"],
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France": {
        "times_visited": 1,
        "cities_visited": ["Paris", "Nice", "Grenoble"],
    },
    "Germany": {
        "times_visited": 7,
        "cities_visited": ["Berlin", "Stuttgart"],
    },
}

print(travel_log["Germany"]["cities_visited"][1])

