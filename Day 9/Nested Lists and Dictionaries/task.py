
capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

travel_log = {
    "France": ["Paris", "Nice", "Grenoble"],
    "Germany": ["Berlin", "Stuttgart"],
}

print(travel_log["France"][1])

nested_list = ["A", "B",["C", "D"]]

print(nested_list[2][1])


travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Nice", "Grenoble"],
    },
    "Germany": ["Berlin", "Stuttgart"],
}

print(travel_log["France"]["cities_visited"][2])