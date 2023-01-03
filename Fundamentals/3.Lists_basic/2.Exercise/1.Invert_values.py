list_original = input().split(" ")
new_list = list()

for n in list_original:
    n = int(n)
    new_n = n * -1
    new_list.append(new_n)

print(new_list)
