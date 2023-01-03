#string_names_list = input().split(", ")
#sorted_list = list(sorted(string_names_list, key=len))
#new_list = list()
#for i in range(1, len(sorted_list) + 1):
#    current_name = sorted_list[-i]
#    new_list.append(current_name)
#
#print(new_list)
#
#THAT WAS MY TRY...

names_list = input().split(", ")
sorted_list = sorted(names_list, key=lambda x: (-len(x), x))
print(sorted_list)
