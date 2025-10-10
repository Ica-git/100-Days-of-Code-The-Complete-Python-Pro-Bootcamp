import random
#new_dict = {new_key:new_value for item in list}

#new_dict = {new_key:new_value for (key, value) in dict.items()}

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# student_scores = {student:random.randint(1,100) for student in names}
#
# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
#
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# words = sentence.split()
#
# result = {word:len(word) for word in words}


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
#
# print(weather_f)

# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Alex":
#         print(row.score)

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

#print(df)

#new_dict = {new_key:new_value for (key, value) in dict.item()}

#new_dict = {letter:code for (index, row) in df.iterrows()}

# for (key, value) in df.items():
#     print(value)

# for (index, row) in df.iterrows():
#     print(row)

# bid = int(input("What is your bid?: $"))
#     bids[name] = bid

# for (index, row) in df.iterrows():
#     print(row.letter)
#     print(row.code)

alfabet = {row.letter: row.code for index, row in df.iterrows()}

# for (index, row) in df.iterrows():
#     alfabet[row.letter] = row.code

def generate_phonetic():
    word = input("What is your word?: ").upper()

    try:
        end_list = [alfabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(end_list)

generate_phonetic()

# for letter in word:
#     end_list.append(alfabet[letter])










