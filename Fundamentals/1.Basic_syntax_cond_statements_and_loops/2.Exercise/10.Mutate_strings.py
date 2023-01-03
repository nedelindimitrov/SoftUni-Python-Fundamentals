first_string = list(input())
second_string = list(input())

len_of_str = len(first_string)

for i in range(len_of_str):
    first_symbol = first_string[i]
    second_symbol = second_string[i]
    this_word = ""

    if first_symbol != second_symbol:
        first_string[i] = second_symbol
        for y in first_string:
            this_word += y
        print(this_word)
        continue
    else:
        continue
