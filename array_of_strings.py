array_of_strings = ["hello", "2", "world", ":-)"]
str_meet_the_requirements = []
index = 0
while index != len(array_of_strings):
    if len(array_of_strings[index]) <= 3:
        str_meet_the_requirements.append(array_of_strings[index])
    index += 1
print(str_meet_the_requirements)