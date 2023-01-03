string = input()
new_string = ""

previous_char = ""

for i in range(len(string)):
    current_char = string[i]

    if previous_char != current_char:
        new_string += current_char

    previous_char = current_char

print(new_string)
