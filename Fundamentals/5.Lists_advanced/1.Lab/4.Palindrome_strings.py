input_random_list = input().split(" ")
palindrome_search = input()
found_palindrome_counter = 0
new_edited_list = list()

for i in range(len(input_random_list)):
    current_check = input_random_list[i]
    reversed_check = current_check[::-1]
    if current_check == reversed_check:
        new_edited_list.append(current_check)


for t in range(len(new_edited_list)):
    current_new_check = new_edited_list[t]
    if current_new_check == palindrome_search:
        found_palindrome_counter += 1

print(new_edited_list)
print(f"Found palindrome {found_palindrome_counter} times")
