number = int(input())
key_word = input()

first_list = list()
second_list = list()

for n in range(number):
    current_string = input()
    first_list.append(current_string)
    if key_word in current_string:
        second_list.append(current_string)

print(first_list)
print(second_list)
